typedef struct _cups_dir_s cups_dir_t;	
typedef struct cups_dentry_s cups_dentry_t;
void		cupsDirClose(cups_dir_t *dp);
cups_dir_t	*cupsDirOpen(const char *directory);
cups_dentry_t	*cupsDirRead(cups_dir_t *dp);
void		cupsDirRewind(cups_dir_t *dp);
