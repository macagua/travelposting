# Generated by Django 2.1.11 on 2020-09-03 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0056_auto_20200901_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='country',
            field=models.CharField(choices=[('TF', 'French Southern Territories'), ('RS', 'Serbia'), ('CX', 'Christmas Island'), ('JP', 'Japan'), ('MG', 'Madagascar'), ('KZ', 'Kazakhstan'), ('SE', 'Sweden'), ('ES', 'Spain'), ('SA', 'Saudi Arabia'), ('DM', 'Dominica'), ('CY', 'Cyprus'), ('WS', 'Samoa'), ('CI', "Côte d'Ivoire"), ('AE', 'United Arab Emirates'), ('ST', 'Sao Tome and Principe'), ('TZ', 'Tanzania, the United Republic of'), ('AR', 'Argentina'), ('SG', 'Singapore'), ('SB', 'Solomon Islands'), ('KN', 'Saint Kitts and Nevis'), ('ZM', 'Zambia'), ('IT', 'Italy'), ('BD', 'Bangladesh'), ('UZ', 'Uzbekistan'), ('LI', 'Liechtenstein'), ('GU', 'Guam'), ('FO', 'Faroe Islands'), ('KW', 'Kuwait'), ('ET', 'Ethiopia'), ('LY', 'Libya'), ('NO', 'Norway'), ('FK', 'Falkland Islands (Malvinas)'), ('AU', 'Australia'), ('EH', 'Western Sahara'), ('JO', 'Jordan'), ('SO', 'Somalia'), ('QA', 'Qatar'), ('CR', 'Costa Rica'), ('TM', 'Turkmenistan'), ('JE', 'Jersey'), ('NC', 'New Caledonia'), ('EE', 'Estonia'), ('BI', 'Burundi'), ('MN', 'Mongolia'), ('SM', 'San Marino'), ('NU', 'Niue'), ('CN', 'China'), ('TD', 'Chad'), ('CG', 'Congo'), ('TO', 'Tonga'), ('GL', 'Greenland'), ('UM', 'United States Minor Outlying Islands'), ('MM', 'Myanmar'), ('MK', 'North Macedonia'), ('SN', 'Senegal'), ('MZ', 'Mozambique'), ('VC', 'Saint Vincent and the Grenadines'), ('TN', 'Tunisia'), ('PY', 'Paraguay'), ('GR', 'Greece'), ('LR', 'Liberia'), ('PF', 'French Polynesia'), ('SI', 'Slovenia'), ('SR', 'Suriname'), ('US', 'United States of America'), ('NE', 'Niger'), ('DE', 'Germany'), ('BS', 'Bahamas'), ('NR', 'Nauru'), ('CD', 'Congo (the Democratic Republic of the)'), ('UG', 'Uganda'), ('AD', 'Andorra'), ('GE', 'Georgia'), ('RW', 'Rwanda'), ('KE', 'Kenya'), ('GH', 'Ghana'), ('MS', 'Montserrat'), ('BT', 'Bhutan'), ('TR', 'Turkey'), ('MC', 'Monaco'), ('ZA', 'South Africa'), ('GI', 'Gibraltar'), ('NF', 'Norfolk Island'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('BM', 'Bermuda'), ('HT', 'Haiti'), ('BY', 'Belarus'), ('BW', 'Botswana'), ('TK', 'Tokelau'), ('NG', 'Nigeria'), ('IQ', 'Iraq'), ('BH', 'Bahrain'), ('BG', 'Bulgaria'), ('CF', 'Central African Republic'), ('TL', 'Timor-Leste'), ('BF', 'Burkina Faso'), ('HK', 'Hong Kong'), ('NP', 'Nepal'), ('IO', 'British Indian Ocean Territory'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('LV', 'Latvia'), ('MW', 'Malawi'), ('FI', 'Finland'), ('GD', 'Grenada'), ('AQ', 'Antarctica'), ('KM', 'Comoros'), ('AX', 'Åland Islands'), ('SV', 'El Salvador'), ('AW', 'Aruba'), ('TJ', 'Tajikistan'), ('GT', 'Guatemala'), ('CA', 'Canada'), ('GN', 'Guinea'), ('UA', 'Ukraine'), ('DK', 'Denmark'), ('PM', 'Saint Pierre and Miquelon'), ('MQ', 'Martinique'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('TV', 'Tuvalu'), ('MX', 'Mexico'), ('BZ', 'Belize'), ('RU', 'Russian Federation'), ('MD', 'Moldova (the Republic of)'), ('FJ', 'Fiji'), ('VI', 'Virgin Islands (U.S.)'), ('PK', 'Pakistan'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('PL', 'Poland'), ('CC', 'Cocos (Keeling) Islands'), ('BO', 'Bolivia (Plurinational State of)'), ('ER', 'Eritrea'), ('HM', 'Heard Island and McDonald Islands'), ('KI', 'Kiribati'), ('LB', 'Lebanon'), ('LA', "Lao People's Democratic Republic"), ('HR', 'Croatia'), ('BE', 'Belgium'), ('DZ', 'Algeria'), ('IR', 'Iran (Islamic Republic of)'), ('MU', 'Mauritius'), ('ME', 'Montenegro'), ('UY', 'Uruguay'), ('IN', 'India'), ('VU', 'Vanuatu'), ('AI', 'Anguilla'), ('CU', 'Cuba'), ('CV', 'Cabo Verde'), ('MH', 'Marshall Islands'), ('FM', 'Micronesia (Federated States of)'), ('KY', 'Cayman Islands'), ('CO', 'Colombia'), ('VA', 'Holy See'), ('FR', 'France'), ('MV', 'Maldives'), ('IL', 'Israel'), ('BN', 'Brunei Darussalam'), ('GF', 'French Guiana'), ('SK', 'Slovakia'), ('BR', 'Brazil'), ('AO', 'Angola'), ('CW', 'Curaçao'), ('MT', 'Malta'), ('MF', 'Saint Martin (French part)'), ('EC', 'Ecuador'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('SY', 'Syrian Arab Republic'), ('PN', 'Pitcairn'), ('PW', 'Palau'), ('MO', 'Macao'), ('PR', 'Puerto Rico'), ('GP', 'Guadeloupe'), ('AL', 'Albania'), ('CK', 'Cook Islands'), ('AG', 'Antigua and Barbuda'), ('RO', 'Romania'), ('WF', 'Wallis and Futuna'), ('HN', 'Honduras'), ('AT', 'Austria'), ('ID', 'Indonesia'), ('NI', 'Nicaragua'), ('HU', 'Hungary'), ('ZW', 'Zimbabwe'), ('ML', 'Mali'), ('GY', 'Guyana'), ('MR', 'Mauritania'), ('KG', 'Kyrgyzstan'), ('OM', 'Oman'), ('TG', 'Togo'), ('SD', 'Sudan'), ('SX', 'Sint Maarten (Dutch part)'), ('SJ', 'Svalbard and Jan Mayen'), ('CM', 'Cameroon'), ('EG', 'Egypt'), ('YT', 'Mayotte'), ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('GM', 'Gambia'), ('IE', 'Ireland'), ('CL', 'Chile'), ('GW', 'Guinea-Bissau'), ('PA', 'Panama'), ('PH', 'Philippines'), ('TT', 'Trinidad and Tobago'), ('LC', 'Saint Lucia'), ('MA', 'Morocco'), ('TC', 'Turks and Caicos Islands'), ('BV', 'Bouvet Island'), ('PT', 'Portugal'), ('SL', 'Sierra Leone'), ('DJ', 'Djibouti'), ('AZ', 'Azerbaijan'), ('JM', 'Jamaica'), ('LU', 'Luxembourg'), ('GQ', 'Equatorial Guinea'), ('YE', 'Yemen'), ('LT', 'Lithuania'), ('AM', 'Armenia'), ('KR', 'Korea (the Republic of)'), ('IS', 'Iceland'), ('TH', 'Thailand'), ('CH', 'Switzerland'), ('SC', 'Seychelles'), ('AF', 'Afghanistan'), ('PE', 'Peru'), ('VN', 'Viet Nam'), ('PS', 'Palestine, State of'), ('CZ', 'Czechia'), ('RE', 'Réunion'), ('TW', 'Taiwan (Province of China)'), ('SZ', 'Eswatini'), ('KP', "Korea (the Democratic People's Republic of)"), ('LS', 'Lesotho'), ('MY', 'Malaysia'), ('LK', 'Sri Lanka'), ('PG', 'Papua New Guinea'), ('GS', 'South Georgia and the South Sandwich Islands'), ('MP', 'Northern Mariana Islands'), ('GG', 'Guernsey'), ('VG', 'Virgin Islands (British)'), ('GA', 'Gabon'), ('AS', 'American Samoa'), ('SS', 'South Sudan'), ('DO', 'Dominican Republic'), ('IM', 'Isle of Man'), ('BJ', 'Benin'), ('BL', 'Saint Barthélemy'), ('NA', 'Namibia'), ('KH', 'Cambodia')], max_length=3, verbose_name='Countries'),
        ),
    ]