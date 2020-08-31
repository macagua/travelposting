# Generated by Django 2.1.11 on 2020-08-25 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0045_auto_20200810_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='request',
            name='country',
            field=models.CharField(choices=[('NI', 'Nicaragua'), ('TG', 'Togo'), ('VN', 'Viet Nam'), ('LV', 'Latvia'), ('MF', 'Saint Martin (French part)'), ('IO', 'British Indian Ocean Territory'), ('AG', 'Antigua and Barbuda'), ('GY', 'Guyana'), ('QA', 'Qatar'), ('AM', 'Armenia'), ('IR', 'Iran (Islamic Republic of)'), ('VU', 'Vanuatu'), ('DM', 'Dominica'), ('TM', 'Turkmenistan'), ('GU', 'Guam'), ('PS', 'Palestine, State of'), ('AW', 'Aruba'), ('CV', 'Cabo Verde'), ('BH', 'Bahrain'), ('AR', 'Argentina'), ('KI', 'Kiribati'), ('DJ', 'Djibouti'), ('BR', 'Brazil'), ('LU', 'Luxembourg'), ('MW', 'Malawi'), ('GI', 'Gibraltar'), ('HM', 'Heard Island and McDonald Islands'), ('MU', 'Mauritius'), ('SX', 'Sint Maarten (Dutch part)'), ('IE', 'Ireland'), ('BN', 'Brunei Darussalam'), ('WS', 'Samoa'), ('TL', 'Timor-Leste'), ('NZ', 'New Zealand'), ('ER', 'Eritrea'), ('GH', 'Ghana'), ('CG', 'Congo'), ('KM', 'Comoros'), ('SB', 'Solomon Islands'), ('AE', 'United Arab Emirates'), ('BS', 'Bahamas'), ('IL', 'Israel'), ('RS', 'Serbia'), ('GW', 'Guinea-Bissau'), ('CN', 'China'), ('ST', 'Sao Tome and Principe'), ('ES', 'Spain'), ('CL', 'Chile'), ('PY', 'Paraguay'), ('YE', 'Yemen'), ('CI', "Côte d'Ivoire"), ('FM', 'Micronesia (Federated States of)'), ('PT', 'Portugal'), ('BJ', 'Benin'), ('CR', 'Costa Rica'), ('HU', 'Hungary'), ('NP', 'Nepal'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('TJ', 'Tajikistan'), ('TO', 'Tonga'), ('PE', 'Peru'), ('BI', 'Burundi'), ('BD', 'Bangladesh'), ('GA', 'Gabon'), ('TZ', 'Tanzania, the United Republic of'), ('UG', 'Uganda'), ('NL', 'Netherlands'), ('IS', 'Iceland'), ('TF', 'French Southern Territories'), ('PR', 'Puerto Rico'), ('SL', 'Sierra Leone'), ('SC', 'Seychelles'), ('US', 'United States of America'), ('EG', 'Egypt'), ('RU', 'Russian Federation'), ('UY', 'Uruguay'), ('MD', 'Moldova (the Republic of)'), ('FI', 'Finland'), ('BZ', 'Belize'), ('EH', 'Western Sahara'), ('MM', 'Myanmar'), ('JP', 'Japan'), ('SI', 'Slovenia'), ('ID', 'Indonesia'), ('MX', 'Mexico'), ('CO', 'Colombia'), ('YT', 'Mayotte'), ('VA', 'Holy See'), ('IT', 'Italy'), ('TH', 'Thailand'), ('CF', 'Central African Republic'), ('HN', 'Honduras'), ('MK', 'North Macedonia'), ('CH', 'Switzerland'), ('ME', 'Montenegro'), ('PN', 'Pitcairn'), ('UA', 'Ukraine'), ('PK', 'Pakistan'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SR', 'Suriname'), ('SE', 'Sweden'), ('GN', 'Guinea'), ('CM', 'Cameroon'), ('TC', 'Turks and Caicos Islands'), ('CY', 'Cyprus'), ('GG', 'Guernsey'), ('MO', 'Macao'), ('CZ', 'Czechia'), ('FO', 'Faroe Islands'), ('EE', 'Estonia'), ('FR', 'France'), ('PW', 'Palau'), ('CX', 'Christmas Island'), ('LA', "Lao People's Democratic Republic"), ('TT', 'Trinidad and Tobago'), ('UM', 'United States Minor Outlying Islands'), ('BO', 'Bolivia (Plurinational State of)'), ('AU', 'Australia'), ('MH', 'Marshall Islands'), ('SM', 'San Marino'), ('NO', 'Norway'), ('CA', 'Canada'), ('TD', 'Chad'), ('BF', 'Burkina Faso'), ('SV', 'El Salvador'), ('FJ', 'Fiji'), ('RW', 'Rwanda'), ('LY', 'Libya'), ('VC', 'Saint Vincent and the Grenadines'), ('SS', 'South Sudan'), ('TV', 'Tuvalu'), ('GM', 'Gambia'), ('GL', 'Greenland'), ('AT', 'Austria'), ('LT', 'Lithuania'), ('SJ', 'Svalbard and Jan Mayen'), ('BY', 'Belarus'), ('GQ', 'Equatorial Guinea'), ('DO', 'Dominican Republic'), ('TK', 'Tokelau'), ('KG', 'Kyrgyzstan'), ('MQ', 'Martinique'), ('MP', 'Northern Mariana Islands'), ('PG', 'Papua New Guinea'), ('MY', 'Malaysia'), ('GP', 'Guadeloupe'), ('MR', 'Mauritania'), ('GR', 'Greece'), ('BA', 'Bosnia and Herzegovina'), ('AO', 'Angola'), ('CD', 'Congo (the Democratic Republic of the)'), ('KW', 'Kuwait'), ('IM', 'Isle of Man'), ('KZ', 'Kazakhstan'), ('NE', 'Niger'), ('MS', 'Montserrat'), ('AI', 'Anguilla'), ('KR', 'Korea (the Republic of)'), ('LB', 'Lebanon'), ('KY', 'Cayman Islands'), ('RE', 'Réunion'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('ML', 'Mali'), ('AL', 'Albania'), ('TW', 'Taiwan (Province of China)'), ('DE', 'Germany'), ('ET', 'Ethiopia'), ('MV', 'Maldives'), ('ZW', 'Zimbabwe'), ('HR', 'Croatia'), ('KH', 'Cambodia'), ('EC', 'Ecuador'), ('WF', 'Wallis and Futuna'), ('IN', 'India'), ('MA', 'Morocco'), ('UZ', 'Uzbekistan'), ('CK', 'Cook Islands'), ('MC', 'Monaco'), ('BG', 'Bulgaria'), ('PF', 'French Polynesia'), ('GT', 'Guatemala'), ('CC', 'Cocos (Keeling) Islands'), ('GD', 'Grenada'), ('MG', 'Madagascar'), ('PA', 'Panama'), ('BL', 'Saint Barthélemy'), ('AQ', 'Antarctica'), ('HK', 'Hong Kong'), ('FK', 'Falkland Islands (Malvinas)'), ('PH', 'Philippines'), ('VI', 'Virgin Islands (U.S.)'), ('MZ', 'Mozambique'), ('SN', 'Senegal'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('AS', 'American Samoa'), ('GE', 'Georgia'), ('RO', 'Romania'), ('AX', 'Åland Islands'), ('NF', 'Norfolk Island'), ('LS', 'Lesotho'), ('JE', 'Jersey'), ('LR', 'Liberia'), ('NG', 'Nigeria'), ('TR', 'Turkey'), ('NA', 'Namibia'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('CW', 'Curaçao'), ('SD', 'Sudan'), ('IQ', 'Iraq'), ('JM', 'Jamaica'), ('OM', 'Oman'), ('LC', 'Saint Lucia'), ('SO', 'Somalia'), ('AZ', 'Azerbaijan'), ('MN', 'Mongolia'), ('SY', 'Syrian Arab Republic'), ('SG', 'Singapore'), ('PL', 'Poland'), ('BV', 'Bouvet Island'), ('KE', 'Kenya'), ('MT', 'Malta'), ('NC', 'New Caledonia'), ('ZM', 'Zambia'), ('NR', 'Nauru'), ('NU', 'Niue'), ('BT', 'Bhutan'), ('SK', 'Slovakia'), ('KP', "Korea (the Democratic People's Republic of)"), ('DZ', 'Algeria'), ('ZA', 'South Africa'), ('LI', 'Liechtenstein'), ('SA', 'Saudi Arabia'), ('KN', 'Saint Kitts and Nevis'), ('BW', 'Botswana'), ('TN', 'Tunisia'), ('PM', 'Saint Pierre and Miquelon'), ('LK', 'Sri Lanka'), ('HT', 'Haiti'), ('BB', 'Barbados'), ('GF', 'French Guiana'), ('SZ', 'Eswatini'), ('VG', 'Virgin Islands (British)'), ('BM', 'Bermuda'), ('JO', 'Jordan'), ('BE', 'Belgium'), ('AD', 'Andorra'), ('DK', 'Denmark'), ('CU', 'Cuba'), ('AF', 'Afghanistan')], max_length=3, verbose_name='Countries'),
        ),
    ]
