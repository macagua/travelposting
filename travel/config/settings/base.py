import os  # isort:skip
import environ
import telepot
from django.utils.translation import gettext_lazy as _

gettext = lambda s: s

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
ROOT_DIR = (
        environ.Path(__file__) - 3
)

RECAPTCHA_PUBLIC_KEY = '6Ld03sgUAAAAAFj2SbpktazIW-C8bWL2ILCrq-KP'
RECAPTCHA_PRIVATE_KEY = '6Ld03sgUAAAAAE1eCnFqdLCDAKApu4kJH64sSbq7'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
APPS_DIR = ROOT_DIR.path("apps/")

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path(".env")))


# Quick-start development settings - unsuitable for production

# Application definition

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"

MIGRATION_MODULES = {

}

FIXTURE_DIRS = (
   os.path.join(ROOT_DIR, 'fixtures'),
)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('de', gettext('de')),
    ('es', gettext('es'))
)

URL_NAME_LANGS = LANGUAGES

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'


TIME_ZONE = 'America/Caracas'

# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [
    os.path.join(APPS_DIR, 'locale/'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_URL = '/main/media/'
MEDIA_ROOT = os.path.join(os.getcwd(),'main/media/')
STATIC_ROOT = os.path.join(os.getcwd(), 'main/static/')
STATIC_URL = '/static/'
GEOIP_PATH = MEDIA_ROOT + '/GeoLite2'
STATICFILES_DIRS = (
    os.path.join(os.getcwd(), 'main/private/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
)

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'main/templates').replace('\\', '/'),
            os.path.join(os.getcwd(), 'main/templates/'),
            os.path.join(os.getcwd(), 'main/templates/'),
            os.path.join(os.getcwd(), 'main/templates/admin'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'apps.landing_page.context_processor.get_ip',
                'cms.context_processors.cms_settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'apps.community.middleware.CampaignMiddleware'
]

DJANGO_APPS = [
    'djangocms_admin_style',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.gis'
]

THIRD_PARTY = [
    'favicon',
    #below app is here accordinf to the docs for cms
    'apps.accounts.apps.AccountsConfig',
    'cms',
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'taggit',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'mptt',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'django_yubin',
    'djangocms_video',
    'django_summernote',
    'impersonate',
    'rest_framework',
    'nested_admin',
    'rosetta',
    'bootstrap_datepicker_plus',
    'oauth2_provider',
    'mapwidgets',
    'mathfilters',
    'sorl.thumbnail',
    'captcha',
    'django_admin_logs',
    #'notifications',
    'ads.apps.AdsConfig',
    'star_ratings'
]

LOCAL_APPS = [
    'apps.landing_page.apps.LandingPageConfig',
    'apps.utils.apps.UtilsConfig',
    'apps.payments.apps.PaymentsConfig',
    'apps.destinations.apps.DestinationsConfig',
    'apps.api.apps.ApiConfig',
    'apps.community.apps.CommunityConfig',
    'apps.directmessages.apps.DirectmessagesConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + LOCAL_APPS


DJANGO_ADMIN_LOGS_ENABLED = True


# Email config
# https://docs.djangoproject.com/en/2.1/topics/email/#module-django.core.mail
# python -m smtpd -n -c DebuggingServer localhost:1025
ADMINS = [
    ('Eliezer Romero', 'eliezerfot123@gmail.com'),
]

MANAGERS = [
    ('Eliezer Romero', 'eliezerfot123@gmail.com'),
    (_('Travel Dashboard'), 'tablero@travelpostig.com'),
    (_('Support'), 'support@travelpostig.com'),
]

# Authentication options
AUTH_USER_MODEL = 'accounts.CustomerUser'
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'dashboard:dashboard-index'
LOGOUT_URL = 'accounts:logout'
LOGOUT_REDIRECT_URL = 'accounts:logout'

THUMBNAIL_HIGH_RESOLUTION = True

#CMS_LANGUAGES = {
    ## Customize this
 #   1: [
 #       {
 #           'code': 'es',
 #           'name': gettext('es'),
#          'redirect_on_fallback': True,
#            'public': True,
#            'hide_untranslated': False,
#        },
#    ],
#    2: [
#        {
#            'code': 'en',
#            'name': gettext('en'),
#            'redirect_on_fallback': True,
#            'public': True,
#            'hide_untranslated': False,
#        },
#    ],
#    3: [
#        {
#            'code': 'de',
#            'name': gettext('de'),
#            'redirect_on_fallback': True,
#            'public': True,
#            'hide_untranslated': False,
#        },
#    ],
#    'default': {
#        'redirect_on_fallback': True,
#        'public': True,
#        'hide_untranslated': False,
#    },
#}
DJANGOCMS_STYLE_TEMPLATES = [
    ('feature', _('Feature')),
]


CMS_TEMPLATES = (
    ## Customize this
    ('index.html', _('Landing')),
    ('about.html', 'About us'),
    ('template_base_for_text.html', 'Template base'),
    ('tours.html', _('Tour')),
    ('magazine.html', _('Magazine')),
    ('community.html', _('Community')),
    ('datenschutz.html', _('Data protection')),
    ('datenshutz_form.html', _('Data protection Form')),
    ('datenshutz_form_privacity.html', _('Data protection Form Privacity')),
    ('coming-soon.html', _('Coming Soon')),
    ('hotels.html', _('Hotels template')),
    ('pricing.html', _('Pricing')),
    ('make_page.html', 'Make page'),
    ('term.html', _('Terms')),
    ('faq.html',_('FAQ')),
    ('page01.html', _('Page type 01')),
    ('page02.html', _('Page type 02')),
    ('presignup.html', _('Pre-signup')),

)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

# Allow all host domains in DEBUG MODE

KEEP_COMMENTS_ON_MINIFYING = False

CKEDITOR_UPLOAD_PATH = "uploads_ckeditor/"
CKEDITOR_IMAGE_BACKED = 'pillow'

CKEDITOR_SETTINGS = {
    'disableNativeSpellChecker': False,
    'language' : 'es',
    'toolbar': 'Custom',
    'toolbar_Custom': [['Undo', 'Redo'], ["Bold", "Italic", "Underline", "Strike", "SpellChecker", "Subscript", "Superscript"],
                   ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'Blockquote'],
                   ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
                   ["TabErrorle", "Link", "Unlink", "Anchor", "SectionLink"],
                   ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],['TextColor', 'BGColor' ],
                   ['Styles', 'Format', 'Font', 'FontSize' ], ['Maximize', 'ShowBlocks', 'Templates', '-', 'Source']],
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# ROSETTA
# https://django-rosetta.readthedocs.io/
# ------------------------------------------------------------------------------
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
# ROSETTA_SHOW_AT_ADMIN_PANEL = True
ROSETTA_REQUIRES_AUTH = True
ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_UWSGI_AUTO_RELOAD = True


#PRICES SETTINGS:
SHORT_DATE_FORMAT = "d/m/y"
DEFAULT_CURRENCY = 'USD'
CURRENCIES = ('USD', 'EUR')
CURRENCY_DECIMAL_PLACES = 2
CURRENCY_CHOICES = [
    ('USD', 'USD $'),
    ('EUR', 'EUR €'),
]

# File upload
# Archivos de maximo 5 megas.
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880
DATA_UPLOAD_MAX_MEMORY_SIZE = 6291456

# Django Summernote config
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'lazy': True,
    'js': (
        'destinations/js/summernote-map-plugin.js',
    )
}


# Config Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': ('rest_framework.pagination.PageNumberPagination',),
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Oauth2 Provider
OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Permiso de lectura',
        'write': 'Permiso de escritura'
    }
}

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django_yubin.smtp_queue.EmailBackend'


#FOR GOOGLE-MAP-WIDGETS
#https://django-map-widgets.readthedocs.io/en/latest/widgets/point_field_map_widgets.html#usage

GOOGLE_MAPS_API_KEY = env('GOOGLE_MAPS_API_KEY', default="AIzaSyB_CmhhFa-mzxnprFS9hxgfY5Fh_IsHpoo")

MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocationName", "london"),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": GOOGLE_MAPS_API_KEY,
}

CAMPAIGN_COUPON_PREFIX = 'TPCW-20'
CAMPAIGN_COUPON_LIMIT = 10000

BOT = telepot.Bot('806633169:AAFouKIb9-QwJvGnLz6eIjO3rDBLB4HT78M')


# Django Star Ratings System
# https://django-star-ratings.readthedocs.io/

# To change the star icon height, defaults to 32
STAR_RATINGS_STAR_HEIGHT = 12
