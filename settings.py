# Django settings for edc project.

import os.path

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Akshit Khurana', 'axitkhurana@gmail.com'),
    ('Vikesh Khanna', 'khanna.vikesh@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/home/axitkhurana/db/edc.sql',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
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

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media'

# for CK Editor plugin
STATIC_URL = MEDIA_URL
CKEDITOR_MEDIA_PREFIX = "media/ckeditor/"
CKEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), "media/uploads/ckeditor")

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '04e@jm7ge+x83@(!g(%21e!(ac8sgljlo*8kn1xkj=1k$g3+26'

# RECAPTCHA_PUBLIC_KEY = '6LfzZtcSAAAAALAeNAvthwBoERw_VBTcvZbIvTYC'
# RECAPTCHA_PRIVATE_KEY = '6LfzZtcSAAAAAMphQIhI9E16Y2knTHPzDo-W7Kmt'
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
)

ROOT_URLCONF = 'edc.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages"
)

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'edciitr'
EMAIL_HOST_PASSWORD = 'edciitrnumber1'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = "noreply@edciitr.com"
SERVER_EMAIL = "admin@domain.com"
EMAIL_USE_TLS = False

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    "/home/edciitr/webapps/django/edc/templates/",
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
    'home',
    'events',
    'about',
    'users',
    'resources',
    'recruitments',
    'confirm',
    'haystack',
    'associates',
    'ckeditor',
    'feedback',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# haystack settings
HAYSTACK_SITECONF = 'haystack.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(os.path.dirname(__file__), 'haystack/whoosh')
HAYSTACK_LIMIT_TO_REGISTERED_MODELS = False

CKEDITOR_CONFIGS = {
    'admin': {
        'toolbar': 'Full',
        'width': 1000,
        'height': 200,
    },
    'arth': {
        'toolbar': 'Basic',
        'width': 800,
        'height': 200,
    },
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': 300,
    },
}
