from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core import validators
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from apps.landing_page.models import Plan
from apps.utils.views import get_referal_code

from random import randint
import uuid


DEGRE_CHOICES = (
    ('sra', _('Mrs.')),
    ('sr', _('Mr.')),
    ('divers', _('Divers')),
    ('dr', _('Dr.')),
    ('prof', _('Prof.')),
    ('lic', _('Lic.')),
    ('agrupacion', _('Grouping')),
    ('prof-dr', _('Prof. Dr.'))
)

COUNTRIES = {
    ("AF", _("Afghanistan")),
    ("AX", _("Åland Islands")),
    ("AL", _("Albania")),
    ("DZ", _("Algeria")),
    ("AS", _("American Samoa")),
    ("AD", _("Andorra")),
    ("AO", _("Angola")),
    ("AI", _("Anguilla")),
    ("AQ", _("Antarctica")),
    ("AG", _("Antigua and Barbuda")),
    ("AR", _("Argentina")),
    ("AM", _("Armenia")),
    ("AW", _("Aruba")),
    ("AU", _("Australia")),
    ("AT", _("Austria")),
    ("AZ", _("Azerbaijan")),
    ("BS", _("Bahamas")),
    ("BH", _("Bahrain")),
    ("BD", _("Bangladesh")),
    ("BB", _("Barbados")),
    ("BY", _("Belarus")),
    ("BE", _("Belgium")),
    ("BZ", _("Belize")),
    ("BJ", _("Benin")),
    ("BM", _("Bermuda")),
    ("BT", _("Bhutan")),
    ("BO", _("Bolivia (Plurinational State of)")),
    ("BQ", _("Bonaire, Sint Eustatius and Saba")),
    ("BA", _("Bosnia and Herzegovina")),
    ("BW", _("Botswana")),
    ("BV", _("Bouvet Island")),
    ("BR", _("Brazil")),
    ("IO", _("British Indian Ocean Territory")),
    ("BN", _("Brunei Darussalam")),
    ("BG", _("Bulgaria")),
    ("BF", _("Burkina Faso")),
    ("BI", _("Burundi")),
    ("CV", _("Cabo Verde")),
    ("KH", _("Cambodia")),
    ("CM", _("Cameroon")),
    ("CA", _("Canada")),
    ("KY", _("Cayman Islands")),
    ("CF", _("Central African Republic")),
    ("TD", _("Chad")),
    ("CL", _("Chile")),
    ("CN", _("China")),
    ("CX", _("Christmas Island")),
    ("CC", _("Cocos (Keeling) Islands")),
    ("CO", _("Colombia")),
    ("KM", _("Comoros")),
    ("CG", _("Congo")),
    ("CD", _("Congo (the Democratic Republic of the)")),
    ("CK", _("Cook Islands")),
    ("CR", _("Costa Rica")),
    ("CI", _("Côte d'Ivoire")),
    ("HR", _("Croatia")),
    ("CU", _("Cuba")),
    ("CW", _("Curaçao")),
    ("CY", _("Cyprus")),
    ("CZ", _("Czechia")),
    ("DK", _("Denmark")),
    ("DJ", _("Djibouti")),
    ("DM", _("Dominica")),
    ("DO", _("Dominican Republic")),
    ("EC", _("Ecuador")),
    ("EG", _("Egypt")),
    ("SV", _("El Salvador")),
    ("GQ", _("Equatorial Guinea")),
    ("ER", _("Eritrea")),
    ("EE", _("Estonia")),
    ("SZ", _("Eswatini")),
    ("ET", _("Ethiopia")),
    ("FK", _("Falkland Islands (Malvinas)")),
    ("FO", _("Faroe Islands")),
    ("FJ", _("Fiji")),
    ("FI", _("Finland")),
    ("FR", _("France")),
    ("GF", _("French Guiana")),
    ("PF", _("French Polynesia")),
    ("TF", _("French Southern Territories")),
    ("GA", _("Gabon")),
    ("GM", _("Gambia")),
    ("GE", _("Georgia")),
    ("DE", _("Germany")),
    ("GH", _("Ghana")),
    ("GI", _("Gibraltar")),
    ("GR", _("Greece")),
    ("GL", _("Greenland")),
    ("GD", _("Grenada")),
    ("GP", _("Guadeloupe")),
    ("GU", _("Guam")),
    ("GT", _("Guatemala")),
    ("GG", _("Guernsey")),
    ("GN", _("Guinea")),
    ("GW", _("Guinea-Bissau")),
    ("GY", _("Guyana")),
    ("HT", _("Haiti")),
    ("HM", _("Heard Island and McDonald Islands")),
    ("VA", _("Holy See")),
    ("HN", _("Honduras")),
    ("HK", _("Hong Kong")),
    ("HU", _("Hungary")),
    ("IS", _("Iceland")),
    ("IN", _("India")),
    ("ID", _("Indonesia")),
    ("IR", _("Iran (Islamic Republic of)")),
    ("IQ", _("Iraq")),
    ("IE", _("Ireland")),
    ("IM", _("Isle of Man")),
    ("IL", _("Israel")),
    ("IT", _("Italy")),
    ("JM", _("Jamaica")),
    ("JP", _("Japan")),
    ("JE", _("Jersey")),
    ("JO", _("Jordan")),
    ("KZ", _("Kazakhstan")),
    ("KE", _("Kenya")),
    ("KI", _("Kiribati")),
    ("KP", _("Korea (the Democratic People's Republic of)")),
    ("KR", _("Korea (the Republic of)")),
    ("KW", _("Kuwait")),
    ("KG", _("Kyrgyzstan")),
    ("LA", _("Lao People's Democratic Republic")),
    ("LV", _("Latvia")),
    ("LB", _("Lebanon")),
    ("LS", _("Lesotho")),
    ("LR", _("Liberia")),
    ("LY", _("Libya")),
    ("LI", _("Liechtenstein")),
    ("LT", _("Lithuania")),
    ("LU", _("Luxembourg")),
    ("MO", _("Macao")),
    ("MG", _("Madagascar")),
    ("MW", _("Malawi")),
    ("MY", _("Malaysia")),
    ("MV", _("Maldives")),
    ("ML", _("Mali")),
    ("MT", _("Malta")),
    ("MH", _("Marshall Islands")),
    ("MQ", _("Martinique")),
    ("MR", _("Mauritania")),
    ("MU", _("Mauritius")),
    ("YT", _("Mayotte")),
    ("MX", _("Mexico")),
    ("FM", _("Micronesia (Federated States of)")),
    ("MD", _("Moldova (the Republic of)")),
    ("MC", _("Monaco")),
    ("MN", _("Mongolia")),
    ("ME", _("Montenegro")),
    ("MS", _("Montserrat")),
    ("MA", _("Morocco")),
    ("MZ", _("Mozambique")),
    ("MM", _("Myanmar")),
    ("NA", _("Namibia")),
    ("NR", _("Nauru")),
    ("NP", _("Nepal")),
    ("NL", _("Netherlands")),
    ("NC", _("New Caledonia")),
    ("NZ", _("New Zealand")),
    ("NI", _("Nicaragua")),
    ("NE", _("Niger")),
    ("NG", _("Nigeria")),
    ("NU", _("Niue")),
    ("NF", _("Norfolk Island")),
    ("MK", _("North Macedonia")),
    ("MP", _("Northern Mariana Islands")),
    ("NO", _("Norway")),
    ("OM", _("Oman")),
    ("PK", _("Pakistan")),
    ("PW", _("Palau")),
    ("PS", _("Palestine, State of")),
    ("PA", _("Panama")),
    ("PG", _("Papua New Guinea")),
    ("PY", _("Paraguay")),
    ("PE", _("Peru")),
    ("PH", _("Philippines")),
    ("PN", _("Pitcairn")),
    ("PL", _("Poland")),
    ("PT", _("Portugal")),
    ("PR", _("Puerto Rico")),
    ("QA", _("Qatar")),
    ("RE", _("Réunion")),
    ("RO", _("Romania")),
    ("RU", _("Russian Federation")),
    ("RW", _("Rwanda")),
    ("BL", _("Saint Barthélemy")),
    ("SH", _("Saint Helena, Ascension and Tristan da Cunha")),
    ("KN", _("Saint Kitts and Nevis")),
    ("LC", _("Saint Lucia")),
    ("MF", _("Saint Martin (French part)")),
    ("PM", _("Saint Pierre and Miquelon")),
    ("VC", _("Saint Vincent and the Grenadines")),
    ("WS", _("Samoa")),
    ("SM", _("San Marino")),
    ("ST", _("Sao Tome and Principe")),
    ("SA", _("Saudi Arabia")),
    ("SN", _("Senegal")),
    ("RS", _("Serbia")),
    ("SC", _("Seychelles")),
    ("SL", _("Sierra Leone")),
    ("SG", _("Singapore")),
    ("SX", _("Sint Maarten (Dutch part)")),
    ("SK", _("Slovakia")),
    ("SI", _("Slovenia")),
    ("SB", _("Solomon Islands")),
    ("SO", _("Somalia")),
    ("ZA", _("South Africa")),
    ("GS", _("South Georgia and the South Sandwich Islands")),
    ("SS", _("South Sudan")),
    ("ES", _("Spain")),
    ("LK", _("Sri Lanka")),
    ("SD", _("Sudan")),
    ("SR", _("Suriname")),
    ("SJ", _("Svalbard and Jan Mayen")),
    ("SE", _("Sweden")),
    ("CH", _("Switzerland")),
    ("SY", _("Syrian Arab Republic")),
    ("TW", _("Taiwan (Province of China)")),
    ("TJ", _("Tajikistan")),
    ("TZ", _("Tanzania, the United Republic of")),
    ("TH", _("Thailand")),
    ("TL", _("Timor-Leste")),
    ("TG", _("Togo")),
    ("TK", _("Tokelau")),
    ("TO", _("Tonga")),
    ("TT", _("Trinidad and Tobago")),
    ("TN", _("Tunisia")),
    ("TR", _("Turkey")),
    ("TM", _("Turkmenistan")),
    ("TC", _("Turks and Caicos Islands")),
    ("TV", _("Tuvalu")),
    ("UG", _("Uganda")),
    ("UA", _("Ukraine")),
    ("AE", _("United Arab Emirates")),
    ("GB", _("United Kingdom of Great Britain and Northern Ireland")),
    ("UM", _("United States Minor Outlying Islands")),
    ("US", _("United States of America")),
    ("UY", _("Uruguay")),
    ("UZ", _("Uzbekistan")),
    ("VU", _("Vanuatu")),
    ("VE", _("Venezuela (Bolivarian Republic of)")),
    ("VN", _("Viet Nam")),
    ("VG", _("Virgin Islands (British)")),
    ("VI", _("Virgin Islands (U.S.)")),
    ("WF", _("Wallis and Futuna")),
    ("EH", _("Western Sahara")),
    ("YE", _("Yemen")),
    ("ZM", _("Zambia")),
    ("ZW", _("Zimbabwe")),
}

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomerUser(AbstractUser):
    username = None

    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        verbose_name=_('Plan'),
        blank=True,
        null=True,
    )

    subscription_id = models.CharField(
        _('Subscription ID'),
        max_length=50,
        blank=True,
        null=True,
        editable=False,
        validators=[validators.MinLengthValidator(3)],
    )

    coupon = models.CharField(
        _('Coupon'),
        max_length=50,
        blank=True,
        null=True,
    )

    business_name = models.CharField(
        _("Company name"),
        max_length=150,
        blank=True,
        null=True,
    )

    business_address = models.CharField(
        _("Commercial address"),
        max_length=150,
        blank=True,
        null=True,
    )

    postal_code = models.CharField(
        _("Postal code"),
        max_length=50,
        blank=True,
        null=True,
    )

    state = models.CharField(
        _("City / State / Parish"),
        max_length=50,
        blank=True,
        null=True,
    )

    country = models.CharField(
        _("Country"),
        choices=COUNTRIES,
        max_length=50,
        blank=True,
        null=True,
    )

    language = models.CharField(
        _("Languages in which you are interested in sending or receiving information"),
        max_length=2,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    comment = models.TextField(
        _("Do you have something to tell us?"),
        blank=True,
        null=True,
    )

    degree = models.CharField(
        _("Title (Contact person)"),
        max_length=20,
        choices=DEGRE_CHOICES,
        blank=True,
        null=True,
    )

    business_position = models.CharField(
        _("Position in the company"),
        max_length=100,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        _("Leave us a phone number where we can contact you"),
        max_length=20,
        blank=True,
        null=True,
    )

    mobile = models.CharField(
        _("Mobile number or WhatsApp"),
        max_length=20,
        blank=True,
        null=True,
    )

    web_site = models.URLField(
        _("Leave us your web address"),
        blank=True,
        null=True,
    )

    ref_code = models.CharField(
        _("Code Referral"),
        max_length=20,
        blank=False,
        default=get_referal_code,
    )

    facebook = models.CharField(
        _("Facebook"),
        max_length=100,
        null=True,
        blank=True,
    )

    instagram = models.CharField(
        _("Instagram"),
        max_length=100,
        null=True,
        blank=True,
    )

    twitter = models.CharField(
        _("Twitter"),
        max_length=100,
        null=True,
        blank=True,
    )

    linkedin = models.CharField(
        _("Linkedin"),
        max_length=100,
        null=True,
        blank=True,
    )

    about_me = models.TextField(
        _("About me"),
        null=True,
        blank=True,
        max_length=2000,
    )

    avatar = models.ImageField(
        _("Avatar"),
        upload_to='avatars/',
        null=True,
        blank=True,
    )

    pinterest = models.URLField(_("Pinterest"), blank=True, null=True)

    is_active = models.BooleanField(_("is active?"), default=True)
    is_staff = models.BooleanField(_("is staff?"), default=False)
    is_superuser = models.BooleanField(_("is superuser?"), default=False)
    is_community = models.BooleanField(_("is community?"), default=True)

    last_ip = models.GenericIPAddressField(protocol='IPv4', verbose_name=_("Last Login IP"), null=True, blank=True)
    location = models.CharField(_("Location"), max_length=50, blank=True, null=True)

    slug = models.SlugField(_("SLUG"), unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def add_slug(self):
        name = self.get_full_name() if not self.business_name else self.business_name
        name = name if name.strip() != '' else uuid.uuid4()
        slug = slugify(name)
        if CustomerUser.objects.filter(slug=slug).exists():
            slug = slugify(name+"-"+str(randint(300,999)))
        self.slug = slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.add_slug()
        super().save(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        # swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse_lazy('accounts:user-details', kwargs={'pk': self.pk})


class LastVisitIP(models.Model):
    user = models.ForeignKey(CustomerUser, verbose_name=_("User"), on_delete=models.CASCADE)
    last_ip_login = models.GenericIPAddressField(_("Last Login IP"), protocol='IPv4', null=True, blank=True)
    location = models.CharField(_("Location"),max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Last Visit IP")
        verbose_name_plural = _("Lasts Visits IP")

    @classmethod
    def add(self, user):
        last, new = self.objects.get_or_create(
                user=user,
                last_ip_login=user.last_ip,
                defaults={
                    'location': user.location
                    })

    def __str__(self):
        return self.last_ip_login

    def str(self):
        return str(self.user) +" "+ str(self.last_ip_login)

### Model to interact between one user and another
'''
The preceding code shows the Contact model we will use for user relationships. It contains the following fields:

-> user_from: ForeignKey for the user that creates the relationship
-> user_to: ForeignKey for the user being followed
-> created: A DateTimeField field with auto_now_add=True to store the time when the relationship was created

'''
class Contact(models.Model):
    user_from = models.ForeignKey('accounts.CustomerUser',
                                  verbose_name=_('User that creates the relationship'),
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('accounts.CustomerUser',
                                verbose_name=_('User being followed'),
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(_('Created at'),
                                   auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return _('%(user_from)s follows %(user_to)s') % {
            'user_from': self.user_from,
            'user_to': self.user_to
        }


# Add following field to User dynamically
CustomerUser.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))


from apps.destinations.models import Destination

class Comment(models.Model):
    post = models.ForeignKey(
        Destination, verbose_name=_('Post'),
        related_name='comments', on_delete=None)
    user_comment = models.ForeignKey(
        CustomerUser,
        verbose_name=_('User Comment'),
        max_length=80,
        related_name='user_comment_to',
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    user_answer = models.ForeignKey(
        CustomerUser,
        verbose_name=_('User Answer'),
        max_length=80,
        related_name='user_answer_to',
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=200, null=False, blank=False)
    body = models.TextField(_('Body Comment'))
    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)
    active = models.BooleanField(_('Active'), default=True)
    parent = models.IntegerField(
        _('Parent'),
        null=True,
        blank=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, verbose_name=_('Likes'), blank=True, related_name='post_likes')
    height_field = models.IntegerField(_('Height'), default=0)
    width_field = models.IntegerField(_('Width'), default=0)


    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return _('Comment by %(body)s') % {'body': self.body}