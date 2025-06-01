typedef struct pwg_map_s		
{
  char	*pwg, *ppd;
} pwg_map_t;
typedef struct pwg_media_s		
{
  const char *pwg, *ppd;
	int width, length;
} pwg_media_t;
typedef struct pwg_size_s		
{
  pwg_map_t	map;
	int width,			/* Width in 2540ths */
	length,			/* Length in 2540ths */
	left,			/* Left margin in 2540ths */
	bottom,			/* Bottom margin in 2540ths */
	right,			/* Right margin in 2540ths */
	top;		
} pwg_size_t;
bool		pwgFormatSizeName(char *keyword, size_t keysize, const char *prefix, const char *name, int width, int length, const char *units);
bool		pwgInitSize(pwg_size_t *size, ipp_t *job, bool *margins_set);
pwg_media_t	*pwgMediaForLegacy(const char *legacy);
pwg_media_t	*pwgMediaForPPD(const char *ppd);
pwg_media_t	*pwgMediaForPWG(const char *pwg);
pwg_media_t	*pwgMediaForSize(int width, int length);
