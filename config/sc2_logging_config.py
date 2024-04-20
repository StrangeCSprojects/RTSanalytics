import logging.config
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %I:%M %p'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'WARNING'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/sc2.log',
            'formatter': 'standard',
            'level': 'DEBUG'
        },
        'sc2_comparing_builds': {
            'class': 'logging.FileHandler',
            'filename': 'logs/sc2_comparing_builds.log',
            'formatter': 'standard',
            'level': 'DEBUG'
        },
        'analyze_builds': {
            'class': 'logging.FileHandler',
            'filename': 'logs/sc2_analyze_builds.log',
            'formatter': 'standard',
            'level': 'DEBUG'
        },
        'sc2reader': {
            'class': 'logging.FileHandler',
            'filename': 'logs/sc2reader_errors.log',
            'formatter': 'standard',
            'level': 'DEBUG'  
        }
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'sc2_comparing_builds': {  
            'handlers': ['sc2_comparing_builds'],
            'level': 'DEBUG',
            'propagate': False
        },
        'analyze_builds': {  
            'handlers': ['analyze_builds'],
            'level': 'DEBUG',
            'propagate': False
        },
        'sc2reader': {  # Logger for sc2reader
            'handlers': ['sc2reader'],
            'level': 'DEBUG',
            'propagate': True  # Prevents higher level loggers from also logging these messages
        }
    }
}
def setup_logging():
    # Insert the LOGGING_CONFIG dictionary here
    logging.config.dictConfig(LOGGING_CONFIG)
