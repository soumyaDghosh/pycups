typedef enum cups_adv_e			
{
  CUPS_ADVANCE_NONE = 0,		
  CUPS_ADVANCE_FILE = 1,		
  CUPS_ADVANCE_JOB = 2,			
  CUPS_ADVANCE_SET = 3,			
  CUPS_ADVANCE_PAGE = 4			
} cups_adv_t;
typedef enum cups_bool_e		
{
  CUPS_FALSE = 0,			
  CUPS_TRUE = 1				
} cups_bool_t;
typedef enum cups_cspace_e		
{
  CUPS_CSPACE_W = 0,			
  CUPS_CSPACE_RGB = 1,			
  CUPS_CSPACE_RGBA = 2,			
  CUPS_CSPACE_K = 3,			
  CUPS_CSPACE_CMY = 4,			
  CUPS_CSPACE_YMC = 5,			
  CUPS_CSPACE_CMYK = 6,			
  CUPS_CSPACE_YMCK = 7,			
  CUPS_CSPACE_KCMY = 8,			
  CUPS_CSPACE_KCMYcm = 9,		
  CUPS_CSPACE_GMCK = 10,		
  CUPS_CSPACE_GMCS = 11,		
  CUPS_CSPACE_WHITE = 12,		
  CUPS_CSPACE_GOLD = 13,		
  CUPS_CSPACE_SILVER = 14,		
  CUPS_CSPACE_CIEXYZ = 15,		
  CUPS_CSPACE_CIELab = 16,		
  CUPS_CSPACE_RGBW = 17,		
  CUPS_CSPACE_SW = 18,			
  CUPS_CSPACE_SRGB = 19,		
  CUPS_CSPACE_ADOBERGB = 20,		
  CUPS_CSPACE_ICC1 = 32,		
  CUPS_CSPACE_ICC2 = 33,		
  CUPS_CSPACE_ICC3 = 34,		
  CUPS_CSPACE_ICC4 = 35,		
  CUPS_CSPACE_ICC5 = 36,		
  CUPS_CSPACE_ICC6 = 37,		
  CUPS_CSPACE_ICC7 = 38,		
  CUPS_CSPACE_ICC8 = 39,		
  CUPS_CSPACE_ICC9 = 40,		
  CUPS_CSPACE_ICCA = 41,		
  CUPS_CSPACE_ICCB = 42,		
  CUPS_CSPACE_ICCC = 43,		
  CUPS_CSPACE_ICCD = 44,		
  CUPS_CSPACE_ICCE = 45,		
  CUPS_CSPACE_ICCF = 46,		
  CUPS_CSPACE_DEVICE1 = 48,		
  CUPS_CSPACE_DEVICE2 = 49,		
  CUPS_CSPACE_DEVICE3 = 50,		
  CUPS_CSPACE_DEVICE4 = 51,		
  CUPS_CSPACE_DEVICE5 = 52,		
  CUPS_CSPACE_DEVICE6 = 53,		
  CUPS_CSPACE_DEVICE7 = 54,		
  CUPS_CSPACE_DEVICE8 = 55,		
  CUPS_CSPACE_DEVICE9 = 56,		
  CUPS_CSPACE_DEVICEA = 57,		
  CUPS_CSPACE_DEVICEB = 58,		
  CUPS_CSPACE_DEVICEC = 59,		
  CUPS_CSPACE_DEVICED = 60,		
  CUPS_CSPACE_DEVICEE = 61,		
  CUPS_CSPACE_DEVICEF = 62		
} cups_cspace_t;
typedef enum cups_cut_e			
{
  CUPS_CUT_NONE = 0,			
  CUPS_CUT_FILE = 1,			
  CUPS_CUT_JOB = 2,			
  CUPS_CUT_SET = 3,			
  CUPS_CUT_PAGE = 4			
} cups_cut_t;
typedef enum cups_edge_e		
{
  CUPS_EDGE_TOP = 0,			
  CUPS_EDGE_RIGHT = 1,			
  CUPS_EDGE_BOTTOM = 2,			
  CUPS_EDGE_LEFT = 3			
} cups_edge_t;
typedef enum cups_jog_e			
{
  CUPS_JOG_NONE = 0,			
  CUPS_JOG_FILE = 1,			
  CUPS_JOG_JOB = 2,			
  CUPS_JOG_SET = 3			
} cups_jog_t;
typedef enum cups_mediapos_e		
{
  CUPS_MEDIAPOS_AUTO,			
  CUPS_MEDIAPOS_MAIN,			
  CUPS_MEDIAPOS_ALTERNATE,		
  CUPS_MEDIAPOS_LARGE_CAPACITY,		
  CUPS_MEDIAPOS_MANUAL,			
  CUPS_MEDIAPOS_ENVELOPE,		
  CUPS_MEDIAPOS_DISC,			
  CUPS_MEDIAPOS_PHOTO,			
  CUPS_MEDIAPOS_HAGAKI,			
  CUPS_MEDIAPOS_MAIN_ROLL,		
  CUPS_MEDIAPOS_ALTERNATE_ROLL,		
  CUPS_MEDIAPOS_TOP,			
  CUPS_MEDIAPOS_MIDDLE,			
  CUPS_MEDIAPOS_BOTTOM,			
  CUPS_MEDIAPOS_SIDE,			
  CUPS_MEDIAPOS_LEFT,			
  CUPS_MEDIAPOS_RIGHT,			
  CUPS_MEDIAPOS_CENTER,			
  CUPS_MEDIAPOS_REAR,			
  CUPS_MEDIAPOS_BY_PASS_TRAY,		
  CUPS_MEDIAPOS_TRAY_1,			
  CUPS_MEDIAPOS_TRAY_2,			
  CUPS_MEDIAPOS_TRAY_3,			
  CUPS_MEDIAPOS_TRAY_4,			
  CUPS_MEDIAPOS_TRAY_5,			
  CUPS_MEDIAPOS_TRAY_6,			
  CUPS_MEDIAPOS_TRAY_7,			
  CUPS_MEDIAPOS_TRAY_8,			
  CUPS_MEDIAPOS_TRAY_9,			
  CUPS_MEDIAPOS_TRAY_10,		
  CUPS_MEDIAPOS_TRAY_11,		
  CUPS_MEDIAPOS_TRAY_12,		
  CUPS_MEDIAPOS_TRAY_13,		
  CUPS_MEDIAPOS_TRAY_14,		
  CUPS_MEDIAPOS_TRAY_15,		
  CUPS_MEDIAPOS_TRAY_16,		
  CUPS_MEDIAPOS_TRAY_17,		
  CUPS_MEDIAPOS_TRAY_18,		
  CUPS_MEDIAPOS_TRAY_19,		
  CUPS_MEDIAPOS_TRAY_20,		
  CUPS_MEDIAPOS_ROLL_1,			
  CUPS_MEDIAPOS_ROLL_2,			
  CUPS_MEDIAPOS_ROLL_3,			
  CUPS_MEDIAPOS_ROLL_4,			
  CUPS_MEDIAPOS_ROLL_5,			
  CUPS_MEDIAPOS_ROLL_6,			
  CUPS_MEDIAPOS_ROLL_7,			
  CUPS_MEDIAPOS_ROLL_8,			
  CUPS_MEDIAPOS_ROLL_9,			
  CUPS_MEDIAPOS_ROLL_10			
} cups_mediapos_t;
typedef enum cups_order_e		
{
  CUPS_ORDER_CHUNKED = 0,		
  CUPS_ORDER_BANDED = 1,		
  CUPS_ORDER_PLANAR = 2			
} cups_order_t;
typedef enum cups_orient_e		
{
  CUPS_ORIENT_0 = 0,			
  CUPS_ORIENT_90 = 1,			
  CUPS_ORIENT_180 = 2,			
  CUPS_ORIENT_270 = 3			
} cups_orient_t;
typedef enum cups_raster_mode_e		
{
  CUPS_RASTER_READ = 0,			
  CUPS_RASTER_WRITE = 1,		
  CUPS_RASTER_WRITE_COMPRESSED = 2,	
  CUPS_RASTER_WRITE_PWG = 3,		
  CUPS_RASTER_WRITE_APPLE = 4		
} cups_raster_mode_t;
typedef struct cups_page_header_s	cups_page_header_t;
typedef struct _cups_raster_s cups_raster_t;
typedef ssize_t (*cups_raster_cb_t)(void *ctx, unsigned char *buffer, size_t length);
void		cupsRasterClose(cups_raster_t *r);
const char	*cupsRasterGetErrorString(void);
bool		cupsRasterInitHeader(cups_page_header_t *h, cups_media_t *media, const char *optimize, ipp_quality_t quality, const char *intent, ipp_orient_t orientation, const char *sides, const char *type, int xdpi, int ydpi, const char *sheet_back);
cups_raster_t	*cupsRasterOpen(int fd, cups_raster_mode_t mode);
cups_raster_t	*cupsRasterOpenIO(cups_raster_cb_t iocb, void *ctx, cups_raster_mode_t mode);
bool		cupsRasterReadHeader(cups_raster_t *r, cups_page_header_t *h);
unsigned		cupsRasterReadPixels(cups_raster_t *r, unsigned char *p, unsigned len);
bool		cupsRasterWriteHeader(cups_raster_t *r, cups_page_header_t *h);
unsigned		cupsRasterWritePixels(cups_raster_t *r, unsigned char *p, unsigned len);
