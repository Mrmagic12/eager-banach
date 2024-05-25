"""
Django settings for inventory project.

Generated by 'djangocms' command using django CMS 4.1.0 and Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of Django settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/

For the list of django CMS settings and their values, see
https://docs.django-cms.org/en/release-4.1.x/reference/configuration.html
"""

import os
from pathlib import Path

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5d@gwyyhvg-uf=z2x5ics55hm=^&#=px+l-i@49=(&)o473bn("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['d45jv9-8000.csb.app', 'dy9qmw-8000.csb.app']

CSRF_FAILUER_VIEW = 'myapp.views.my_csrf_failure_view'

CSRF_TRUSTED_SECURE = True

CSRF_TRUSTED_ORIGINS = ['https://d45jv9-8000.csb.app',
                        'https://dy9qmw-8000.csb.app']

CORS_ALLOW_ALL_ORIGINS = True

DJANGOCMS_SNIPPET_SEARCH = True

DJANGOCMS_SNIPPET_THEME = 'github'
DJANGOCMS_SNIPPET_MODE = 'html'
# Application definition

INSTALLED_APPS = [
    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # CMS base apps
    "cms",
    "menus",
    "djangocms_text_ckeditor",
    "djangocms_alias",
    "djangocms_versioning",
    "sekizai",
    "treebeard",
    "parler",
    "filer",
    "easy_thumbnails",
    "djangocms_frontend",
    "djangocms_frontend.contrib.accordion",
    "djangocms_frontend.contrib.alert",
    "djangocms_frontend.contrib.badge",
    "djangocms_frontend.contrib.card",
    "djangocms_frontend.contrib.carousel",
    "djangocms_frontend.contrib.collapse",
    "djangocms_frontend.contrib.content",
    "djangocms_frontend.contrib.grid",
    "djangocms_frontend.contrib.icon",
    "djangocms_frontend.contrib.image",
    "djangocms_frontend.contrib.jumbotron",
    "djangocms_frontend.contrib.link",
    "djangocms_frontend.contrib.listgroup",
    "djangocms_frontend.contrib.media",
    "djangocms_frontend.contrib.navigation",
    "djangocms_frontend.contrib.tabs",
    "djangocms_frontend.contrib.utilities",
    "attendance"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]

ROOT_URLCONF = "inventory.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "inventory", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "cms.context_processors.cms_settings",
            ],
        },
    },
]

DJANGOCMS_FILE_TEMPLATES = [
    ('feature', _('Feature Version')),
]

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

WSGI_APPLICATION = "inventory.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", _("English")),
    ("fr", _("French")),
    ("es", _("Spanish")),
    ("de", _("German")),
    ("it", _("Italian")),
    ("ja", _("Japanese")),
    ("ko", _("Korean")),
    ("ru", _("Russian")),
    ("zh-hans", _("Simplified Chinese")),
    ("zh-hant", _("Traditional Chinese")),
    ("pt-br", _("Brazilian Portuguese")),
    ("pl", _("Polish")),
    ("nl", _("Dutch")),
    ("tr", _("Turkish")),
    ("sv", _("Swedish")),
    ("uk", _("Ukrainian")),
    ("vi", _("Vietnamese")),
    ("fa", _("Persian")),
    ("hi", _("Hindi")),
    ("bn", _("Bengali")),
    ("mr", _("Marathi")),
    ("ta", _("Tamil")),
    ("te", _("Telugu")),
    ("th", _("Thai"))
]

TIME_ZONE = "UTC"

USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# This is a django CMS 4 template

CMS_CONFIRM_VERSION4 = True

# django CMS requires the site framework
# https://docs.django-cms.org/en/release-4.1.x/how_to/multi-site.html

SITE_ID = 1

# A base template is part of this setup
# https://docs.django-cms.org/en/release-4.1.x/reference/configuration.html#cms-templates

CMS_TEMPLATES = (("base.html", _("Standard")),)

# Enable permissions
# https://docs.django-cms.org/en/release-4.1.x/topics/permissions.html

CMS_PERMISSION = True

# Allow admin sidebar to open admin URLs

X_FRAME_OPTIONS = "SAMEORIGIN"

# Enable inline editing with djangocms-text-ckeditor
# https://github.com/django-cms/djangocms-text-ckeditor#inline-editing-feature

TEXT_INLINE_EDITING = True

# Add project-wide static files directory
# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-dirs

STATICFILES_DIRS = [
    BASE_DIR / "inventory" / "static",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# Add project-wide static files directory
# https://docs.djangoproject.com/en/4.2/ref/settings/#media-root

MEDIA_URL = "media/"
MEDIA_ROOT = str(BASE_DIR.parent / "media")
