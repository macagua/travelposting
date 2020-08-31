# Generated by Django 2.1.11 on 2020-08-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0050_merge_20200828_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='country',
            field=models.CharField(choices=[('PR', 'Puerto Rico'), ('EG', 'Egypt'), ('PT', 'Portugal'), ('BO', 'Bolivia (Plurinational State of)'), ('RE', 'Réunion'), ('SO', 'Somalia'), ('AF', 'Afghanistan'), ('GS', 'South Georgia and the South Sandwich Islands'), ('AZ', 'Azerbaijan'), ('LC', 'Saint Lucia'), ('IS', 'Iceland'), ('EC', 'Ecuador'), ('ML', 'Mali'), ('CZ', 'Czechia'), ('MN', 'Mongolia'), ('NO', 'Norway'), ('AX', 'Åland Islands'), ('LU', 'Luxembourg'), ('SB', 'Solomon Islands'), ('HK', 'Hong Kong'), ('MO', 'Macao'), ('PY', 'Paraguay'), ('RW', 'Rwanda'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('NU', 'Niue'), ('TH', 'Thailand'), ('TR', 'Turkey'), ('JE', 'Jersey'), ('MR', 'Mauritania'), ('CW', 'Curaçao'), ('FM', 'Micronesia (Federated States of)'), ('AM', 'Armenia'), ('SZ', 'Eswatini'), ('AL', 'Albania'), ('BR', 'Brazil'), ('UY', 'Uruguay'), ('AT', 'Austria'), ('PM', 'Saint Pierre and Miquelon'), ('UM', 'United States Minor Outlying Islands'), ('BF', 'Burkina Faso'), ('KY', 'Cayman Islands'), ('CY', 'Cyprus'), ('BE', 'Belgium'), ('GQ', 'Equatorial Guinea'), ('BY', 'Belarus'), ('JO', 'Jordan'), ('MF', 'Saint Martin (French part)'), ('PS', 'Palestine, State of'), ('FJ', 'Fiji'), ('BA', 'Bosnia and Herzegovina'), ('RU', 'Russian Federation'), ('MP', 'Northern Mariana Islands'), ('AU', 'Australia'), ('TM', 'Turkmenistan'), ('IT', 'Italy'), ('CD', 'Congo (the Democratic Republic of the)'), ('SR', 'Suriname'), ('KP', "Korea (the Democratic People's Republic of)"), ('VN', 'Viet Nam'), ('EH', 'Western Sahara'), ('AG', 'Antigua and Barbuda'), ('EE', 'Estonia'), ('GI', 'Gibraltar'), ('HT', 'Haiti'), ('LB', 'Lebanon'), ('MY', 'Malaysia'), ('AO', 'Angola'), ('DK', 'Denmark'), ('GM', 'Gambia'), ('PK', 'Pakistan'), ('GE', 'Georgia'), ('BB', 'Barbados'), ('SK', 'Slovakia'), ('MC', 'Monaco'), ('JP', 'Japan'), ('CR', 'Costa Rica'), ('CA', 'Canada'), ('LR', 'Liberia'), ('MW', 'Malawi'), ('FR', 'France'), ('TZ', 'Tanzania, the United Republic of'), ('YT', 'Mayotte'), ('CK', 'Cook Islands'), ('VA', 'Holy See'), ('CN', 'China'), ('KN', 'Saint Kitts and Nevis'), ('CM', 'Cameroon'), ('DZ', 'Algeria'), ('LK', 'Sri Lanka'), ('BZ', 'Belize'), ('GL', 'Greenland'), ('GR', 'Greece'), ('GU', 'Guam'), ('CO', 'Colombia'), ('ID', 'Indonesia'), ('MT', 'Malta'), ('VG', 'Virgin Islands (British)'), ('MK', 'North Macedonia'), ('MG', 'Madagascar'), ('HM', 'Heard Island and McDonald Islands'), ('IQ', 'Iraq'), ('BS', 'Bahamas'), ('NP', 'Nepal'), ('AD', 'Andorra'), ('NL', 'Netherlands'), ('GF', 'French Guiana'), ('SM', 'San Marino'), ('ME', 'Montenegro'), ('TL', 'Timor-Leste'), ('LV', 'Latvia'), ('KM', 'Comoros'), ('DM', 'Dominica'), ('KI', 'Kiribati'), ('MX', 'Mexico'), ('BH', 'Bahrain'), ('SS', 'South Sudan'), ('SD', 'Sudan'), ('UZ', 'Uzbekistan'), ('WF', 'Wallis and Futuna'), ('SG', 'Singapore'), ('BT', 'Bhutan'), ('BN', 'Brunei Darussalam'), ('RS', 'Serbia'), ('MS', 'Montserrat'), ('PW', 'Palau'), ('LI', 'Liechtenstein'), ('AE', 'United Arab Emirates'), ('VC', 'Saint Vincent and the Grenadines'), ('SN', 'Senegal'), ('SY', 'Syrian Arab Republic'), ('LA', "Lao People's Democratic Republic"), ('KE', 'Kenya'), ('AR', 'Argentina'), ('DJ', 'Djibouti'), ('BI', 'Burundi'), ('GP', 'Guadeloupe'), ('FO', 'Faroe Islands'), ('TK', 'Tokelau'), ('LS', 'Lesotho'), ('GD', 'Grenada'), ('GY', 'Guyana'), ('IR', 'Iran (Islamic Republic of)'), ('PE', 'Peru'), ('CI', "Côte d'Ivoire"), ('AI', 'Anguilla'), ('BM', 'Bermuda'), ('UG', 'Uganda'), ('NR', 'Nauru'), ('YE', 'Yemen'), ('NF', 'Norfolk Island'), ('ZW', 'Zimbabwe'), ('AW', 'Aruba'), ('ER', 'Eritrea'), ('RO', 'Romania'), ('ZM', 'Zambia'), ('HR', 'Croatia'), ('FK', 'Falkland Islands (Malvinas)'), ('MV', 'Maldives'), ('IM', 'Isle of Man'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('NE', 'Niger'), ('ET', 'Ethiopia'), ('NC', 'New Caledonia'), ('IE', 'Ireland'), ('HN', 'Honduras'), ('KG', 'Kyrgyzstan'), ('TF', 'French Southern Territories'), ('FI', 'Finland'), ('PH', 'Philippines'), ('TT', 'Trinidad and Tobago'), ('ST', 'Sao Tome and Principe'), ('OM', 'Oman'), ('SI', 'Slovenia'), ('CL', 'Chile'), ('MA', 'Morocco'), ('BV', 'Bouvet Island'), ('TC', 'Turks and Caicos Islands'), ('NI', 'Nicaragua'), ('PL', 'Poland'), ('UA', 'Ukraine'), ('TO', 'Tonga'), ('MM', 'Myanmar'), ('GW', 'Guinea-Bissau'), ('SE', 'Sweden'), ('IO', 'British Indian Ocean Territory'), ('CV', 'Cabo Verde'), ('AQ', 'Antarctica'), ('GA', 'Gabon'), ('CX', 'Christmas Island'), ('CG', 'Congo'), ('MU', 'Mauritius'), ('CH', 'Switzerland'), ('CC', 'Cocos (Keeling) Islands'), ('MD', 'Moldova (the Republic of)'), ('HU', 'Hungary'), ('TG', 'Togo'), ('CU', 'Cuba'), ('GG', 'Guernsey'), ('QA', 'Qatar'), ('PN', 'Pitcairn'), ('SL', 'Sierra Leone'), ('TW', 'Taiwan (Province of China)'), ('KW', 'Kuwait'), ('VU', 'Vanuatu'), ('TV', 'Tuvalu'), ('NZ', 'New Zealand'), ('LY', 'Libya'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('SC', 'Seychelles'), ('AS', 'American Samoa'), ('TN', 'Tunisia'), ('NA', 'Namibia'), ('LT', 'Lithuania'), ('SX', 'Sint Maarten (Dutch part)'), ('PA', 'Panama'), ('ES', 'Spain'), ('BD', 'Bangladesh'), ('MZ', 'Mozambique'), ('SV', 'El Salvador'), ('KH', 'Cambodia'), ('GT', 'Guatemala'), ('PF', 'French Polynesia'), ('US', 'United States of America'), ('IL', 'Israel'), ('MH', 'Marshall Islands'), ('BW', 'Botswana'), ('GH', 'Ghana'), ('SA', 'Saudi Arabia'), ('BL', 'Saint Barthélemy'), ('GN', 'Guinea'), ('JM', 'Jamaica'), ('PG', 'Papua New Guinea'), ('WS', 'Samoa'), ('MQ', 'Martinique'), ('KR', 'Korea (the Republic of)'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('TD', 'Chad'), ('DE', 'Germany'), ('IN', 'India'), ('SJ', 'Svalbard and Jan Mayen'), ('TJ', 'Tajikistan'), ('DO', 'Dominican Republic'), ('KZ', 'Kazakhstan'), ('VI', 'Virgin Islands (U.S.)'), ('NG', 'Nigeria'), ('BJ', 'Benin'), ('CF', 'Central African Republic'), ('BG', 'Bulgaria'), ('ZA', 'South Africa')], max_length=3, verbose_name='Countries'),
        ),
    ]
