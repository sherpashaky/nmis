# Django settings for nmis project.
import os
import sys

CURRENT_FILE = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(CURRENT_FILE)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db.sqlite3',                      # Or path to database file if using sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://localhost:8000/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Login URLs
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/~'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    ('survey_photos', os.path.join(PROJECT_ROOT, 'survey_photos', 'img_storage')),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

COMPRESS_ENABLED = True
CSS_DEBUG_MODE = False

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'mlfs33^s1l4xf6a36$0#j%dd*sisfoi&)&4s-v=91#^l01v)*j'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'user_management.middleware.RequirePermissionMiddleware',
    'user_management.models.UserRequest',
)

# RESTRICTED_URLS and RESTRICTED_URLS_EXCEPTIONS are used by the
# permission middleware in user_management.
RESTRICTED_URLS = (
    (r'^/?$', 'auth.read'),
    (r'^/?~', 'auth.read'),
    (r'^/?facilities/', 'auth.read'),
    (r'^/new_dashboard', 'auth.read'),
    )
RESTRICTED_URLS_EXCEPTIONS = (
    )

ROOT_URLCONF = 'nmis.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'registration',
    'south',
    'compressor',
    'main',
    'uis_r_us',
    'display_defs',
    'xform_manager',
    'nga_districts',
    'facilities',
    'user_management',
)
COMPRESS = True

# Settings for Django Registration
ACCOUNT_ACTIVATION_DAYS = 1

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# 394 - Kaduna/Kachia
# 732 - Kano/Takai
# 366 - Enugu/Isi-Uzo
LIMITED_LGA_LIST = ['366']

SITE_TITLE = "Baseline Data Collection"

TESTING_MODE = False
if len(sys.argv)>=2 and (sys.argv[1]=="test" or sys.argv[1]=="test_all"):
    # This trick works only when we run tests from the command line.
    TESTING_MODE = True
else:
    TESTING_MODE = False

# Clear out the test database
if TESTING_MODE:
    MEDIA_ROOT  = os.path.join(PROJECT_ROOT, 'test_static/')
else:
    MEDIA_ROOT  = os.path.join(PROJECT_ROOT, 'static/')

MAIN_SITE_HOSTNAME = "nmis.mdgs.gov.ng"
DATA_DIR_NAME = 'data'

#If local_settings.py wants to, it can specify extra apps to include
ADDITIONAL_INSTALLED_APPS = ()

try:
    from local_settings import *
except ImportError:
    print("You can override the default settings by adding a "
          "local_settings.py file.")

DATA_DIR = os.path.join(PROJECT_ROOT, DATA_DIR_NAME)
INSTALLED_APPS = tuple(INSTALLED_APPS + ADDITIONAL_INSTALLED_APPS)

# add 'data' to the project if it's a python module
if os.path.exists(os.path.join(DATA_DIR, '__init__.py')):
    INSTALLED_APPS = tuple(INSTALLED_APPS + (DATA_DIR_NAME, ))
