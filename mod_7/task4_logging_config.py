LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO'
        },
        'info_file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'level': 'INFO',
            'filename': 'info_debug.txt'
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'level': 'ERROR',
            'filename': 'error_debug.txt',
            'mode': 'a'
        }
    },
    'loggers': {
        'logger-app': {
            'handlers': ['console', 'info_file', 'error_file'],
            'level': 'INFO'
        }
    }
}