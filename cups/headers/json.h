typedef enum cups_jtype_e		
{
  CUPS_JTYPE_NULL,			
  CUPS_JTYPE_FALSE,			
  CUPS_JTYPE_TRUE,			
  CUPS_JTYPE_NUMBER,			
  CUPS_JTYPE_STRING,			
  CUPS_JTYPE_ARRAY,			
  CUPS_JTYPE_OBJECT,			
  CUPS_JTYPE_KEY			
} cups_jtype_t;
typedef struct _cups_json_s cups_json_t;
void		cupsJSONAdd(cups_json_t *parent, cups_json_t *after, cups_json_t *node);
void		cupsJSONDelete(cups_json_t *json);
bool		cupsJSONExportFile(cups_json_t *json, const char *filename);
char		*cupsJSONExportString(cups_json_t *json);
cups_json_t	*cupsJSONFind(cups_json_t *json, const char *key);
cups_json_t	*cupsJSONGetChild(cups_json_t *json, size_t n);
size_t		cupsJSONGetCount(cups_json_t *json);
const char	*cupsJSONGetKey(cups_json_t *json);
cups_json_t	*cupsJSONGetParent(cups_json_t *json);
cups_json_t	*cupsJSONGetSibling(cups_json_t *json);
double		cupsJSONGetNumber(cups_json_t *json);
const char	*cupsJSONGetString(cups_json_t *json);
cups_jtype_t	cupsJSONGetType(cups_json_t *json);
cups_json_t	*cupsJSONImportFile(const char *filename);
cups_json_t	*cupsJSONImportString(const char *s);
cups_json_t	*cupsJSONImportURL(const char *url, time_t *last_modified);
cups_json_t	*cupsJSONNew(cups_json_t *parent, cups_json_t *after, cups_jtype_t type);
cups_json_t	*cupsJSONNewKey(cups_json_t *parent, cups_json_t *after, const char *value);
cups_json_t	*cupsJSONNewNumber(cups_json_t *parent, cups_json_t *after, double number);
cups_json_t	*cupsJSONNewString(cups_json_t *parent, cups_json_t *after, const char *value);
