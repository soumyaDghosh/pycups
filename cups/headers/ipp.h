typedef void *va_list;
typedef enum ipp_dstate_e		
{
  IPP_DSTATE_PENDING = 3,		
  IPP_DSTATE_PROCESSING = 5,		
  IPP_DSTATE_CANCELED = 7,		
  IPP_DSTATE_ABORTED,			
  IPP_DSTATE_COMPLETED			
} ipp_dstate_t;
typedef enum ipp_finishings_e		
{
  IPP_FINISHINGS_NONE = 3,		
  IPP_FINISHINGS_STAPLE,		
  IPP_FINISHINGS_PUNCH,			
  IPP_FINISHINGS_COVER,			
  IPP_FINISHINGS_BIND,			
  IPP_FINISHINGS_SADDLE_STITCH,		
  IPP_FINISHINGS_EDGE_STITCH,		
  IPP_FINISHINGS_FOLD,			
  IPP_FINISHINGS_TRIM,			
  IPP_FINISHINGS_BALE,			
  IPP_FINISHINGS_BOOKLET_MAKER,		
  IPP_FINISHINGS_JOG_OFFSET,		
  IPP_FINISHINGS_COAT,			
  IPP_FINISHINGS_LAMINATE,		
  IPP_FINISHINGS_STAPLE_TOP_LEFT = 20,	
  IPP_FINISHINGS_STAPLE_BOTTOM_LEFT,	
  IPP_FINISHINGS_STAPLE_TOP_RIGHT,	
  IPP_FINISHINGS_STAPLE_BOTTOM_RIGHT,	
  IPP_FINISHINGS_EDGE_STITCH_LEFT,	
  IPP_FINISHINGS_EDGE_STITCH_TOP,	
  IPP_FINISHINGS_EDGE_STITCH_RIGHT,	
  IPP_FINISHINGS_EDGE_STITCH_BOTTOM,	
  IPP_FINISHINGS_STAPLE_DUAL_LEFT,	
  IPP_FINISHINGS_STAPLE_DUAL_TOP,	
  IPP_FINISHINGS_STAPLE_DUAL_RIGHT,	
  IPP_FINISHINGS_STAPLE_DUAL_BOTTOM,	
  IPP_FINISHINGS_STAPLE_TRIPLE_LEFT,	
  IPP_FINISHINGS_STAPLE_TRIPLE_TOP,	
  IPP_FINISHINGS_STAPLE_TRIPLE_RIGHT,	
  IPP_FINISHINGS_STAPLE_TRIPLE_BOTTOM,	
  IPP_FINISHINGS_BIND_LEFT = 50,	
  IPP_FINISHINGS_BIND_TOP,		
  IPP_FINISHINGS_BIND_RIGHT,		
  IPP_FINISHINGS_BIND_BOTTOM,		
  IPP_FINISHINGS_TRIM_AFTER_PAGES = 60,	
  IPP_FINISHINGS_TRIM_AFTER_DOCUMENTS,	
  IPP_FINISHINGS_TRIM_AFTER_COPIES,	
  IPP_FINISHINGS_TRIM_AFTER_JOB,	
  IPP_FINISHINGS_PUNCH_TOP_LEFT = 70,	
  IPP_FINISHINGS_PUNCH_BOTTOM_LEFT,	
  IPP_FINISHINGS_PUNCH_TOP_RIGHT,	
  IPP_FINISHINGS_PUNCH_BOTTOM_RIGHT,	
  IPP_FINISHINGS_PUNCH_DUAL_LEFT,	
  IPP_FINISHINGS_PUNCH_DUAL_TOP,	
  IPP_FINISHINGS_PUNCH_DUAL_RIGHT,	
  IPP_FINISHINGS_PUNCH_DUAL_BOTTOM,	
  IPP_FINISHINGS_PUNCH_TRIPLE_LEFT,	
  IPP_FINISHINGS_PUNCH_TRIPLE_TOP,	
  IPP_FINISHINGS_PUNCH_TRIPLE_RIGHT,	
  IPP_FINISHINGS_PUNCH_TRIPLE_BOTTOM,	
  IPP_FINISHINGS_PUNCH_QUAD_LEFT,	
  IPP_FINISHINGS_PUNCH_QUAD_TOP,	
  IPP_FINISHINGS_PUNCH_QUAD_RIGHT,	
  IPP_FINISHINGS_PUNCH_QUAD_BOTTOM,	
  IPP_FINISHINGS_PUNCH_MULTIPLE_LEFT,	
  IPP_FINISHINGS_PUNCH_MULTIPLE_TOP,	
  IPP_FINISHINGS_PUNCH_MULTIPLE_RIGHT,	
  IPP_FINISHINGS_PUNCH_MULTIPLE_BOTTOM,	
  IPP_FINISHINGS_FOLD_ACCORDION = 90,	
  IPP_FINISHINGS_FOLD_DOUBLE_GATE,	
  IPP_FINISHINGS_FOLD_GATE,		
  IPP_FINISHINGS_FOLD_HALF,		
  IPP_FINISHINGS_FOLD_HALF_Z,		
  IPP_FINISHINGS_FOLD_LEFT_GATE,	
  IPP_FINISHINGS_FOLD_LETTER,		
  IPP_FINISHINGS_FOLD_PARALLEL,		
  IPP_FINISHINGS_FOLD_POSTER,		
  IPP_FINISHINGS_FOLD_RIGHT_GATE,	
  IPP_FINISHINGS_FOLD_Z,		
  IPP_FINISHINGS_FOLD_ENGINEERING_Z,	
  IPP_FINISHINGS_CUPS_PUNCH_TOP_LEFT = 0x40000046,
  IPP_FINISHINGS_CUPS_PUNCH_BOTTOM_LEFT,
  IPP_FINISHINGS_CUPS_PUNCH_TOP_RIGHT,	
  IPP_FINISHINGS_CUPS_PUNCH_BOTTOM_RIGHT,
  IPP_FINISHINGS_CUPS_PUNCH_DUAL_LEFT,	
  IPP_FINISHINGS_CUPS_PUNCH_DUAL_TOP,	
  IPP_FINISHINGS_CUPS_PUNCH_DUAL_RIGHT,	
  IPP_FINISHINGS_CUPS_PUNCH_DUAL_BOTTOM,
  IPP_FINISHINGS_CUPS_PUNCH_TRIPLE_LEFT,
  IPP_FINISHINGS_CUPS_PUNCH_TRIPLE_TOP,	
  IPP_FINISHINGS_CUPS_PUNCH_TRIPLE_RIGHT,
  IPP_FINISHINGS_CUPS_PUNCH_TRIPLE_BOTTOM,
  IPP_FINISHINGS_CUPS_PUNCH_QUAD_LEFT,	
  IPP_FINISHINGS_CUPS_PUNCH_QUAD_TOP,	
  IPP_FINISHINGS_CUPS_PUNCH_QUAD_RIGHT,	
  IPP_FINISHINGS_CUPS_PUNCH_QUAD_BOTTOM,
  IPP_FINISHINGS_CUPS_FOLD_ACCORDION = 0x4000005A,
  IPP_FINISHINGS_CUPS_FOLD_DOUBLE_GATE,	
  IPP_FINISHINGS_CUPS_FOLD_GATE,	
  IPP_FINISHINGS_CUPS_FOLD_HALF,	
  IPP_FINISHINGS_CUPS_FOLD_HALF_Z,	
  IPP_FINISHINGS_CUPS_FOLD_LEFT_GATE,	
  IPP_FINISHINGS_CUPS_FOLD_LETTER,	
  IPP_FINISHINGS_CUPS_FOLD_PARALLEL,	
  IPP_FINISHINGS_CUPS_FOLD_POSTER,	
  IPP_FINISHINGS_CUPS_FOLD_RIGHT_GATE,	
  IPP_FINISHINGS_CUPS_FOLD_Z		
} ipp_finishings_t;
typedef enum ipp_jstate_e		
{
  IPP_JSTATE_PENDING = 3,		
  IPP_JSTATE_HELD,			
  IPP_JSTATE_PROCESSING,		
  IPP_JSTATE_STOPPED,			
  IPP_JSTATE_CANCELED,			
  IPP_JSTATE_ABORTED,			
  IPP_JSTATE_COMPLETED			
} ipp_jstate_t;
typedef enum ipp_op_e			
{
  IPP_OP_CUPS_INVALID = -1,		
  IPP_OP_CUPS_NONE = 0,			
  IPP_OP_PRINT_JOB = 0x0002,		
  IPP_OP_PRINT_URI,			
  IPP_OP_VALIDATE_JOB,			
  IPP_OP_CREATE_JOB,			
  IPP_OP_SEND_DOCUMENT,			
  IPP_OP_SEND_URI,			
  IPP_OP_CANCEL_JOB,			
  IPP_OP_GET_JOB_ATTRIBUTES,		
  IPP_OP_GET_JOBS,			
  IPP_OP_GET_PRINTER_ATTRIBUTES,	
  IPP_OP_HOLD_JOB,			
  IPP_OP_RELEASE_JOB,			
  IPP_OP_RESTART_JOB,			
  IPP_OP_PAUSE_PRINTER = 0x0010,	
  IPP_OP_RESUME_PRINTER,		
  IPP_OP_PURGE_JOBS,			
  IPP_OP_SET_PRINTER_ATTRIBUTES,	
  IPP_OP_SET_JOB_ATTRIBUTES,		
  IPP_OP_GET_PRINTER_SUPPORTED_VALUES,	
  IPP_OP_CREATE_PRINTER_SUBSCRIPTIONS,	
  IPP_OP_CREATE_JOB_SUBSCRIPTIONS,	
  IPP_OP_GET_SUBSCRIPTION_ATTRIBUTES,	
  IPP_OP_GET_SUBSCRIPTIONS,		
  IPP_OP_RENEW_SUBSCRIPTION,		
  IPP_OP_CANCEL_SUBSCRIPTION,		
  IPP_OP_GET_NOTIFICATIONS,		
  IPP_OP_SEND_NOTIFICATIONS,		
  IPP_OP_GET_RESOURCE_ATTRIBUTES,	
  IPP_OP_GET_RESOURCE_DATA,		
  IPP_OP_GET_RESOURCES,			
  IPP_OP_GET_PRINT_SUPPORT_FILES,	
  IPP_OP_ENABLE_PRINTER,		
  IPP_OP_DISABLE_PRINTER,		
  IPP_OP_PAUSE_PRINTER_AFTER_CURRENT_JOB,
  IPP_OP_HOLD_NEW_JOBS,			
  IPP_OP_RELEASE_HELD_NEW_JOBS,		
  IPP_OP_DEACTIVATE_PRINTER,		
  IPP_OP_ACTIVATE_PRINTER,		
  IPP_OP_RESTART_PRINTER,		
  IPP_OP_SHUTDOWN_PRINTER,		
  IPP_OP_STARTUP_PRINTER,		
  IPP_OP_REPROCESS_JOB,			
  IPP_OP_CANCEL_CURRENT_JOB,		
  IPP_OP_SUSPEND_CURRENT_JOB,		
  IPP_OP_RESUME_JOB,			
  IPP_OP_PROMOTE_JOB,			
  IPP_OP_SCHEDULE_JOB_AFTER,		
  IPP_OP_CANCEL_DOCUMENT = 0x0033,	
  IPP_OP_GET_DOCUMENT_ATTRIBUTES,	
  IPP_OP_GET_DOCUMENTS,			
  IPP_OP_DELETE_DOCUMENT,		
  IPP_OP_SET_DOCUMENT_ATTRIBUTES,	
  IPP_OP_CANCEL_JOBS,			
  IPP_OP_CANCEL_MY_JOBS,		
  IPP_OP_RESUBMIT_JOB,			
  IPP_OP_CLOSE_JOB,			
  IPP_OP_IDENTIFY_PRINTER,		
  IPP_OP_VALIDATE_DOCUMENT,		
  IPP_OP_ADD_DOCUMENT_IMAGES,		
  IPP_OP_ACKNOWLEDGE_DOCUMENT,		
  IPP_OP_ACKNOWLEDGE_IDENTIFY_PRINTER,	
  IPP_OP_ACKNOWLEDGE_JOB,		
  IPP_OP_FETCH_DOCUMENT,		
  IPP_OP_FETCH_JOB,			
  IPP_OP_GET_OUTPUT_DEVICE_ATTRIBUTES,	
  IPP_OP_UPDATE_ACTIVE_JOBS,		
  IPP_OP_DEREGISTER_OUTPUT_DEVICE,	
  IPP_OP_UPDATE_DOCUMENT_STATUS,	
  IPP_OP_UPDATE_JOB_STATUS,		
  IPP_OP_UPDATE_OUTPUT_DEVICE_ATTRIBUTES,
  IPP_OP_GET_NEXT_DOCUMENT_DATA,	
  IPP_OP_ALLOCATE_PRINTER_RESOURCES,    
  IPP_OP_CREATE_PRINTER,                
  IPP_OP_DEALLOCATE_PRINTER_RESOURCES,  
  IPP_OP_DELETE_PRINTER,                
  IPP_OP_GET_PRINTERS,                  
  IPP_OP_SHUTDOWN_ONE_PRINTER,          
  IPP_OP_STARTUP_ONE_PRINTER,           
  IPP_OP_CANCEL_RESOURCE,               
  IPP_OP_CREATE_RESOURCE,               
  IPP_OP_INSTALL_RESOURCE,              
  IPP_OP_SEND_RESOURCE_DATA,            
  IPP_OP_SET_RESOURCE_ATTRIBUTES,       
  IPP_OP_CREATE_RESOURCE_SUBSCRIPTIONS, 
  IPP_OP_CREATE_SYSTEM_SUBSCRIPTIONS,   
  IPP_OP_DISABLE_ALL_PRINTERS,          
  IPP_OP_ENABLE_ALL_PRINTERS,           
  IPP_OP_GET_SYSTEM_ATTRIBUTES,         
  IPP_OP_GET_SYSTEM_SUPPORTED_VALUES,   
  IPP_OP_PAUSE_ALL_PRINTERS,            
  IPP_OP_PAUSE_ALL_PRINTERS_AFTER_CURRENT_JOB,
  IPP_OP_REGISTER_OUTPUT_DEVICE,        
  IPP_OP_RESTART_SYSTEM,                
  IPP_OP_RESUME_ALL_PRINTERS,           
  IPP_OP_SET_SYSTEM_ATTRIBUTES,         
  IPP_OP_SHUTDOWN_ALL_PRINTERS,         
  IPP_OP_STARTUP_ALL_PRINTERS,          
  IPP_OP_GET_PRINTER_RESOURCES,		
  IPP_OP_GET_USER_PRINTER_ATTRIBUTES,	
  IPP_OP_RESTART_ONE_PRINTER,		
  IPP_OP_ACKNOWLEDGE_ENCRYPTED_JOB_ATTRIBUTES,
  IPP_OP_FETCH_ENCRYPTED_JOB_ATTRIBUTES,
  IPP_OP_GET_ENCRYPTED_JOB_ATTRIBUTES,	
  IPP_OP_PRIVATE = 0x4000,		
  IPP_OP_CUPS_GET_DEFAULT,		
  IPP_OP_CUPS_GET_PRINTERS,		
  IPP_OP_CUPS_ADD_MODIFY_PRINTER,	
  IPP_OP_CUPS_DELETE_PRINTER,		
  IPP_OP_CUPS_GET_CLASSES,		
  IPP_OP_CUPS_ADD_MODIFY_CLASS,		
  IPP_OP_CUPS_DELETE_CLASS,		
  IPP_OP_CUPS_ACCEPT_JOBS,		
  IPP_OP_CUPS_REJECT_JOBS,		
  IPP_OP_CUPS_SET_DEFAULT,		
  IPP_OP_CUPS_GET_DEVICES,		
  IPP_OP_CUPS_GET_PPDS,			
  IPP_OP_CUPS_MOVE_JOB,			
  IPP_OP_CUPS_AUTHENTICATE_JOB,		
  IPP_OP_CUPS_GET_PPD,			
  IPP_OP_CUPS_GET_DOCUMENT = 0x4027,	
  IPP_OP_CUPS_CREATE_LOCAL_PRINTER	
} ipp_op_t;
typedef enum ipp_orient_e		
{
  IPP_ORIENT_PORTRAIT = 3,		
  IPP_ORIENT_LANDSCAPE,			
  IPP_ORIENT_REVERSE_LANDSCAPE,		
  IPP_ORIENT_REVERSE_PORTRAIT,		
  IPP_ORIENT_NONE			
} ipp_orient_t;
typedef enum ipp_pstate_e		
{
  IPP_PSTATE_IDLE = 3,			
  IPP_PSTATE_PROCESSING,		
  IPP_PSTATE_STOPPED			
} ipp_pstate_t;
typedef enum ipp_quality_e		
{
  IPP_QUALITY_DRAFT = 3,		
  IPP_QUALITY_NORMAL,			
  IPP_QUALITY_HIGH			
} ipp_quality_t;
typedef enum ipp_res_e			
{
  IPP_RES_PER_INCH = 3,			
  IPP_RES_PER_CM			
} ipp_res_t;
typedef enum ipp_rstate_e		
{
  IPP_RSTATE_PENDING = 3,		
  IPP_RSTATE_AVAILABLE,			
  IPP_RSTATE_INSTALLED,			
  IPP_RSTATE_CANCELED,			
  IPP_RSTATE_ABORTED			
} ipp_rstate_t;
typedef enum ipp_sstate_e		
{
  IPP_SSTATE_IDLE = 3,			
  IPP_SSTATE_PROCESSING,		
  IPP_SSTATE_STOPPED			
} ipp_sstate_t;
typedef enum ipp_state_e		
{
  IPP_STATE_ERROR = -1,			
  IPP_STATE_IDLE,			
  IPP_STATE_HEADER,			
  IPP_STATE_ATTRIBUTE,			
  IPP_STATE_DATA			
} ipp_state_t;
typedef enum ipp_status_e		
{
  IPP_STATUS_CUPS_INVALID = -1,		
  IPP_STATUS_OK = 0x0000,		
  IPP_STATUS_OK_IGNORED_OR_SUBSTITUTED,	
  IPP_STATUS_OK_CONFLICTING,		
  IPP_STATUS_OK_IGNORED_SUBSCRIPTIONS,	
  IPP_STATUS_OK_IGNORED_NOTIFICATIONS,	
  IPP_STATUS_OK_TOO_MANY_EVENTS,	
  IPP_STATUS_OK_BUT_CANCEL_SUBSCRIPTION,
  IPP_STATUS_OK_EVENTS_COMPLETE,	
  IPP_STATUS_REDIRECTION_OTHER_SITE = 0x0200,
  IPP_STATUS_CUPS_SEE_OTHER = 0x0280,	
  IPP_STATUS_ERROR_BAD_REQUEST = 0x0400,
  IPP_STATUS_ERROR_FORBIDDEN,		
  IPP_STATUS_ERROR_NOT_AUTHENTICATED,	
  IPP_STATUS_ERROR_NOT_AUTHORIZED,	
  IPP_STATUS_ERROR_NOT_POSSIBLE,	
  IPP_STATUS_ERROR_TIMEOUT,		
  IPP_STATUS_ERROR_NOT_FOUND,		
  IPP_STATUS_ERROR_GONE,		
  IPP_STATUS_ERROR_REQUEST_ENTITY,	
  IPP_STATUS_ERROR_REQUEST_VALUE,	
  IPP_STATUS_ERROR_DOCUMENT_FORMAT_NOT_SUPPORTED,
  IPP_STATUS_ERROR_ATTRIBUTES_OR_VALUES,
  IPP_STATUS_ERROR_URI_SCHEME,		
  IPP_STATUS_ERROR_CHARSET,		
  IPP_STATUS_ERROR_CONFLICTING,		
  IPP_STATUS_ERROR_COMPRESSION_NOT_SUPPORTED,
  IPP_STATUS_ERROR_COMPRESSION_ERROR,	
  IPP_STATUS_ERROR_DOCUMENT_FORMAT_ERROR,
  IPP_STATUS_ERROR_DOCUMENT_ACCESS,	
  IPP_STATUS_ERROR_ATTRIBUTES_NOT_SETTABLE,
  IPP_STATUS_ERROR_IGNORED_ALL_SUBSCRIPTIONS,
  IPP_STATUS_ERROR_TOO_MANY_SUBSCRIPTIONS,
  IPP_STATUS_ERROR_IGNORED_ALL_NOTIFICATIONS,
  IPP_STATUS_ERROR_PRINT_SUPPORT_FILE_NOT_FOUND,
  IPP_STATUS_ERROR_DOCUMENT_PASSWORD,	
  IPP_STATUS_ERROR_DOCUMENT_PERMISSION,	
  IPP_STATUS_ERROR_DOCUMENT_SECURITY,	
  IPP_STATUS_ERROR_DOCUMENT_UNPRINTABLE,
  IPP_STATUS_ERROR_ACCOUNT_INFO_NEEDED,	
  IPP_STATUS_ERROR_ACCOUNT_CLOSED,	
  IPP_STATUS_ERROR_ACCOUNT_LIMIT_REACHED,
  IPP_STATUS_ERROR_ACCOUNT_AUTHORIZATION_FAILED,
  IPP_STATUS_ERROR_NOT_FETCHABLE,	
  IPP_STATUS_ERROR_INTERNAL = 0x0500,	
  IPP_STATUS_ERROR_OPERATION_NOT_SUPPORTED,
  IPP_STATUS_ERROR_SERVICE_UNAVAILABLE,	
  IPP_STATUS_ERROR_VERSION_NOT_SUPPORTED,
  IPP_STATUS_ERROR_DEVICE,		
  IPP_STATUS_ERROR_TEMPORARY,		
  IPP_STATUS_ERROR_NOT_ACCEPTING_JOBS,	
  IPP_STATUS_ERROR_BUSY,		
  IPP_STATUS_ERROR_JOB_CANCELED,	
  IPP_STATUS_ERROR_MULTIPLE_JOBS_NOT_SUPPORTED,
  IPP_STATUS_ERROR_PRINTER_IS_DEACTIVATED,
  IPP_STATUS_ERROR_TOO_MANY_JOBS,	
  IPP_STATUS_ERROR_TOO_MANY_DOCUMENTS,	
  IPP_STATUS_ERROR_CUPS_AUTHENTICATION_CANCELED = 0x1000,
  IPP_STATUS_ERROR_CUPS_PKI,		
  IPP_STATUS_ERROR_CUPS_UPGRADE_REQUIRED,
  IPP_STATUS_ERROR_CUPS_OAUTH		
} ipp_status_t;
typedef enum ipp_tag_e			
{
  IPP_TAG_CUPS_INVALID = -1,		
  IPP_TAG_ZERO = 0x00,			
  IPP_TAG_OPERATION,			
  IPP_TAG_JOB,				
  IPP_TAG_END,				
  IPP_TAG_PRINTER,			
  IPP_TAG_UNSUPPORTED_GROUP,		
  IPP_TAG_SUBSCRIPTION,			
  IPP_TAG_EVENT_NOTIFICATION,		
  IPP_TAG_RESOURCE,			
  IPP_TAG_DOCUMENT,			
  IPP_TAG_SYSTEM,                       
  IPP_TAG_UNSUPPORTED_VALUE = 0x10,	
  IPP_TAG_DEFAULT,			
  IPP_TAG_UNKNOWN,			
  IPP_TAG_NOVALUE,			
  IPP_TAG_NOTSETTABLE = 0x15,		
  IPP_TAG_DELETEATTR,			
  IPP_TAG_ADMINDEFINE,			
  IPP_TAG_INTEGER = 0x21,		
  IPP_TAG_BOOLEAN,			
  IPP_TAG_ENUM,				
  IPP_TAG_STRING = 0x30,		
  IPP_TAG_DATE,				
  IPP_TAG_RESOLUTION,			
  IPP_TAG_RANGE,			
  IPP_TAG_BEGIN_COLLECTION,		
  IPP_TAG_TEXTLANG,			
  IPP_TAG_NAMELANG,			
  IPP_TAG_END_COLLECTION,		
  IPP_TAG_TEXT = 0x41,			
  IPP_TAG_NAME,				
  IPP_TAG_RESERVED_STRING,		
  IPP_TAG_KEYWORD,			
  IPP_TAG_URI,				
  IPP_TAG_URISCHEME,			
  IPP_TAG_CHARSET,			
  IPP_TAG_LANGUAGE,			
  IPP_TAG_MIMETYPE,			
  IPP_TAG_MEMBERNAME,			
  IPP_TAG_EXTENSION = 0x7f,		
  IPP_TAG_CUPS_MASK = 0x7fffffff,	
  IPP_TAG_CUPS_CONST = -0x7fffffff-1	
} ipp_tag_t;
typedef unsigned char ipp_uchar_t;	
typedef struct _ipp_s ipp_t;		
typedef struct _ipp_attribute_s ipp_attribute_t;
typedef struct _ipp_file_s ipp_file_t;	
typedef bool (*ipp_fattr_cb_t)(ipp_file_t *file, void *cb_data, const char *name);
typedef bool (*ipp_ferror_cb_t)(ipp_file_t *file, void *cb_data, const char *error);
typedef bool (*ipp_ftoken_cb_t)(ipp_file_t *file, void *cb_data, const char *token);
typedef ssize_t	(*ipp_io_cb_t)(void *context, ipp_uchar_t *buffer, size_t bytes);
typedef bool (*ipp_copy_cb_t)(void *context, ipp_t *dst, ipp_attribute_t *attr);
ipp_attribute_t	*ippAddBoolean(ipp_t *ipp, ipp_tag_t group, const char *name, bool value);
ipp_attribute_t	*ippAddBooleans(ipp_t *ipp, ipp_tag_t group, const char *name, size_t num_values, const bool *values);
ipp_attribute_t	*ippAddCollection(ipp_t *ipp, ipp_tag_t group, const char *name, ipp_t *value);
ipp_attribute_t	*ippAddCollections(ipp_t *ipp, ipp_tag_t group, const char *name, size_t num_values, const ipp_t **values);
ipp_attribute_t	*ippAddCredentialsString(ipp_t *ipp, ipp_tag_t group, const char *name, const char *credentials);
ipp_attribute_t	*ippAddDate(ipp_t *ipp, ipp_tag_t group, const char *name, const ipp_uchar_t *value);
ipp_attribute_t	*ippAddInteger(ipp_t *ipp, ipp_tag_t group, ipp_tag_t value_tag, const char *name, int value);
ipp_attribute_t	*ippAddIntegers(ipp_t *ipp, ipp_tag_t group, ipp_tag_t value_tag, const char *name, size_t num_values, const int *values);
ipp_attribute_t	*ippAddOctetString(ipp_t *ipp, ipp_tag_t group, const char *name, const void *data, size_t datalen);
ipp_attribute_t	*ippAddOutOfBand(ipp_t *ipp, ipp_tag_t group, ipp_tag_t value_tag, const char *name);
ipp_attribute_t	*ippAddRange(ipp_t *ipp, ipp_tag_t group, const char *name, int lower, int upper);
ipp_attribute_t	*ippAddRanges(ipp_t *ipp, ipp_tag_t group, const char *name, size_t num_values, const int *lower, const int *upper);
ipp_attribute_t	*ippAddResolution(ipp_t *ipp, ipp_tag_t group, const char *name, ipp_res_t units, int xres, int yres);
ipp_attribute_t	*ippAddResolutions(ipp_t *ipp, ipp_tag_t group, const char *name, size_t num_values, ipp_res_t units, const int *xres, const int *yres);
ipp_attribute_t	*ippAddSeparator(ipp_t *ipp);
ipp_attribute_t	*ippAddString(ipp_t *ipp, ipp_tag_t group, ipp_tag_t value_tag, const char *name, const char *language, const char *value);
ipp_attribute_t	*ippAddStringf(ipp_t *ipp, ipp_tag_t group, ipp_tag_t value_tag, const char *name, const char *language, const char *format, ...);
ipp_attribute_t	*ippAddStringfv(ipp_t *ipp, ipp_tag_t group, ipp_tag_t value_tag, const char *name, const char *language, const char *format, va_list ap);
ipp_attribute_t	*ippAddStrings(ipp_t *ipp, ipp_tag_t group, ipp_tag_t value_tag, const char *name,  size_t num_values, const char *language, const char * const *values);
size_t		ippAttributeString(ipp_attribute_t *attr, char *buffer, size_t bufsize);
bool		ippContainsInteger(ipp_attribute_t *attr, int value);
bool		ippContainsString(ipp_attribute_t *attr, const char *value);
ipp_attribute_t	*ippCopyAttribute(ipp_t *dst, ipp_attribute_t *attr, bool quickcopy);
bool		ippCopyAttributes(ipp_t *dst, ipp_t *src, bool quickcopy, ipp_copy_cb_t cb, void *cb_data);
char		*ippCopyCredentialsString(ipp_attribute_t *attr);
cups_array_t	*ippCreateRequestedArray(ipp_t *request);
time_t		ippDateToTime(const ipp_uchar_t *date);
void		ippDelete(ipp_t *ipp);
void		ippDeleteAttribute(ipp_t *ipp, ipp_attribute_t *attr);
bool		ippDeleteValues(ipp_t *ipp, ipp_attribute_t **attr, size_t element, size_t count);
const char	*ippEnumString(const char *attrname, int enumvalue);
int		ippEnumValue(const char *attrname, const char *enumstring);
const char	*ippErrorString(ipp_status_t error);
ipp_status_t	ippErrorValue(const char *name);
bool		ippFileClose(ipp_file_t *file);
bool		ippFileDelete(ipp_file_t *file);
size_t		ippFileExpandVars(ipp_file_t *file, char *dst, const char *src, size_t dstsize);
ipp_attribute_t	*ippFileGetAttribute(ipp_file_t *file, const char *name, ipp_tag_t value_tag);
ipp_t		*ippFileGetAttributes(ipp_file_t *file);
const char	*ippFileGetFilename(ipp_file_t *file);
int		ippFileGetLineNumber(ipp_file_t *file);
const char	*ippFileGetVar(ipp_file_t *file, const char *name);
ipp_file_t	*ippFileNew(ipp_file_t *parent, ipp_fattr_cb_t attr_cb, ipp_ferror_cb_t error_cb, void *cb_data);
bool		ippFileOpen(ipp_file_t *file, const char *filename, const char *mode);
bool		ippFileRead(ipp_file_t *file, ipp_ftoken_cb_t token_cb, bool with_groups);
ipp_t		*ippFileReadCollection(ipp_file_t *file);
bool		ippFileReadToken(ipp_file_t *file, char *token, size_t tokensize);
bool		ippFileRestorePosition(ipp_file_t *file);
bool		ippFileSavePosition(ipp_file_t *file);
bool		ippFileSetAttributes(ipp_file_t *file, ipp_t *attrs);
bool		ippFileSetGroupTag(ipp_file_t *file, ipp_tag_t group_tag);
bool		ippFileSetVar(ipp_file_t *file, const char *name, const char *value);
bool		ippFileSetVarf(ipp_file_t *file, const char *name, const char *value, ...);
bool		ippFileWriteAttributes(ipp_file_t *file, ipp_t *ipp, bool with_groups);
bool		ippFileWriteComment(ipp_file_t *file, const char *comment, ...);
bool		ippFileWriteToken(ipp_file_t *file, const char *token);
bool		ippFileWriteTokenf(ipp_file_t *file, const char *token, ...);
ipp_attribute_t	*ippFindAttribute(ipp_t *ipp, const char *name, ipp_tag_t value_tag);
ipp_attribute_t	*ippFindNextAttribute(ipp_t *ipp, const char *name, ipp_tag_t value_tag);
bool		ippGetBoolean(ipp_attribute_t *attr, size_t element);
ipp_t		*ippGetCollection(ipp_attribute_t *attr, size_t element);
size_t		ippGetCount(ipp_attribute_t *attr);
const ipp_uchar_t *ippGetDate(ipp_attribute_t *attr, size_t element);
ipp_attribute_t	*ippGetFirstAttribute(ipp_t *ipp);
ipp_tag_t	ippGetGroupTag(ipp_attribute_t *attr);
int		ippGetInteger(ipp_attribute_t *attr, size_t element);
size_t		ippGetLength(ipp_t *ipp);
const char	*ippGetName(ipp_attribute_t *attr);
ipp_attribute_t	*ippGetNextAttribute(ipp_t *ipp);
void		*ippGetOctetString(ipp_attribute_t *attr, size_t element, size_t *datalen);
ipp_op_t		ippGetOperation(ipp_t *ipp);
int		ippGetPort(void);
int		ippGetRange(ipp_attribute_t *attr, size_t element, int *upper);
int		ippGetRequestId(ipp_t *ipp);
int		ippGetResolution(ipp_attribute_t *attr, size_t element, int *yres, ipp_res_t *units);
ipp_state_t	ippGetState(ipp_t *ipp);
ipp_status_t	ippGetStatusCode(ipp_t *ipp);
const char	*ippGetString(ipp_attribute_t *attr, size_t element, const char **language);
ipp_tag_t	ippGetValueTag(ipp_attribute_t *attr);
int		ippGetVersion(ipp_t *ipp, int *minor);
ipp_t		*ippNew(void);
ipp_t		*ippNewRequest(ipp_op_t op);
ipp_t		*ippNewResponse(ipp_t *request);
const char	*ippOpString(ipp_op_t op);
ipp_op_t		ippOpValue(const char *name);
ipp_state_t	ippRead(http_t *http, ipp_t *ipp);
ipp_state_t	ippReadFile(int fd, ipp_t *ipp);
ipp_state_t	ippReadIO(void *src, ipp_io_cb_t cb, bool blocking, ipp_t *parent, ipp_t *ipp);
void		ippRestore(ipp_t *ipp);
void		ippSave(ipp_t *ipp);
bool		ippSetBoolean(ipp_t *ipp, ipp_attribute_t **attr, size_t element, bool boolvalue);
bool		ippSetCollection(ipp_t *ipp, ipp_attribute_t **attr, size_t element, ipp_t *colvalue);
bool		ippSetDate(ipp_t *ipp, ipp_attribute_t **attr, size_t element, const ipp_uchar_t *datevalue);
bool		ippSetGroupTag(ipp_t *ipp, ipp_attribute_t **attr, ipp_tag_t group_tag);
bool		ippSetInteger(ipp_t *ipp, ipp_attribute_t **attr, size_t element, int intvalue);
bool		ippSetName(ipp_t *ipp, ipp_attribute_t **attr, const char *name);
bool		ippSetOctetString(ipp_t *ipp, ipp_attribute_t **attr, size_t element, const void *data, size_t datalen);
bool		ippSetOperation(ipp_t *ipp, ipp_op_t op);
void		ippSetPort(int p);
bool		ippSetRange(ipp_t *ipp, ipp_attribute_t **attr, size_t element, int lowervalue, int uppervalue);
bool		ippSetRequestId(ipp_t *ipp, int request_id);
bool		ippSetResolution(ipp_t *ipp, ipp_attribute_t **attr, size_t element, ipp_res_t unitsvalue, int xresvalue, int yresvalue);
bool		ippSetState(ipp_t *ipp, ipp_state_t state);
bool		ippSetStatusCode(ipp_t *ipp, ipp_status_t status);
bool		ippSetString(ipp_t *ipp, ipp_attribute_t **attr, size_t element, const char *strvalue);
bool		ippSetStringf(ipp_t *ipp, ipp_attribute_t **attr, size_t element, const char *format, ...);
bool		ippSetStringfv(ipp_t *ipp, ipp_attribute_t **attr, size_t element, const char *format, va_list ap);
bool		ippSetValueTag(ipp_t *ipp, ipp_attribute_t **attr, ipp_tag_t value_tag);
bool		ippSetVersion(ipp_t *ipp, int major, int minor);
const char	*ippStateString(ipp_state_t state);
const char	*ippTagString(ipp_tag_t tag);
ipp_tag_t	ippTagValue(const char *name);
const ipp_uchar_t *ippTimeToDate(time_t t);
bool		ippValidateAttribute(ipp_attribute_t *attr);
bool		ippValidateAttributes(ipp_t *ipp);
ipp_state_t	ippWrite(http_t *http, ipp_t *ipp);
ipp_state_t	ippWriteFile(int fd, ipp_t *ipp);
ipp_state_t	ippWriteIO(void *dst, ipp_io_cb_t cb, bool blocking, ipp_t *parent, ipp_t *ipp);
