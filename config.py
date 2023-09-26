visa_currents = """
AED -
AFN -
ALL -
AMD -
ANG -
AOA -
ARS -
AUD -
AWG -
AZN -
BAM -
BBD -
BDT -
BGN -
BHD -
BIF -
BMD -
BND -
BOB -
BRL -
BSD -
BTN -
BWP -
BYN -
BZD -
CAD -
CDF -
CHF -
CLP -
CNY -
COP -
CRC -
CVE -
CYP -
CZK -
DJF -
DKK -
DOP -
DZD -
EEK -
EGP -
ERN -
ETB -
EUR -
FJD -
FKP -
GBP -
GEL -
GHS -
GIP -
GMD -
GNF -
GQE -
GTQ -
GWP -
GYD -
HKD -
HNL -
HRK -
HTG -
HUF -
IDR -
ILS -
INR -
IQD -
IRR -
ISK -
JMD -
JOD -
JPY -
KES -
KGS -
KHR -
KMF -
KRW -
KWD -
KYD -
KZT -
LAK -
LBP -
LKR -
LRD -
LSL -
LTL -
LVL -
LYD -
MAD -
MDL -
MGA -
MKD -
MMK -
MNT -
MOP -
MRO -
MRU -
MTL -
MUR -
MVR -
MWK -
MXN -
MYR -
MZN -
NAD -
NGN -
NIO -
NOK -
NPR -
NZD -
OMR -
PAB -
PEN -
PGK -
PHP -
PKR -
PLN -
PYG -
QAR -
RON -
RSD -
RUB -
RWF -
SAR -
SBD -
SCR -
SDG -
SEK -
SGD -
SHP -
SIT -
SKK -
SLE -
SLL -
SOS -
SRD -
SSP -
STD -
STN -
SVC -
SYP -
SZL -
THB -
TJS -
TMT -
TND -
TOP -
TRY -
TTD -
TWD -
TZS -
UAH -
UGX -
USD -
UYU -
UZS -
VEF -
VES -
VND -
VUV -
WST -
XAF -
XCD -
XOF -
XPF -
YER -
ZAR -
ZMW -
ZWL -
"""
mas_currents_visa = visa_currents.split("-")

cookies_visa = {
    '__cfruid': '16bd63232c395e47a627921a38dfa177e85dc71a-1695718026',
    'wscrCookieConsent': '1=true&2=false&3=false&4=false&5=false&visitor=647a056e-033c-4a65-a469-c1049e1eda5f&version=20230911-001',
    'utag_main': 'v_id:018ad0abb1810098f79892926f180506f005b06700978$_sn:1$_se:33$_ss:0$_st:1695721501932$ses_id:1695718027651%3Bexp-session$_pn:4%3Bexp-session$_prevpage:www.visa.com.kz%2Fru_KZ%2Fsupport%2Fconsumer%2Ftravel-support%2Fexchange-rate-calculator.html%3Bexp-1695723301958',
    'lbs': '!yWpgADleoyIQiS+hTK7BLDNA2UyawAxqLTfXblwsFuXJ17TzZA5HlaZp5BaVQRKDDqbh2Y0pFwkWqZ7sz8jLtXjbttqOTmPtMKwjzgcl',
}

headers_visa = {
    'authority': 'www.visa.com.kz',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    # 'cookie': '__cfruid=16bd63232c395e47a627921a38dfa177e85dc71a-1695718026; wscrCookieConsent=1=true&2=false&3=false&4=false&5=false&visitor=647a056e-033c-4a65-a469-c1049e1eda5f&version=20230911-001; utag_main=v_id:018ad0abb1810098f79892926f180506f005b06700978$_sn:1$_se:33$_ss:0$_st:1695721501932$ses_id:1695718027651%3Bexp-session$_pn:4%3Bexp-session$_prevpage:www.visa.com.kz%2Fru_KZ%2Fsupport%2Fconsumer%2Ftravel-support%2Fexchange-rate-calculator.html%3Bexp-1695723301958; lbs=!yWpgADleoyIQiS+hTK7BLDNA2UyawAxqLTfXblwsFuXJ17TzZA5HlaZp5BaVQRKDDqbh2Y0pFwkWqZ7sz8jLtXjbttqOTmPtMKwjzgcl',
    'referer': 'https://www.visa.com.kz/ru_KZ/support/consumer/travel-support/exchange-rate-calculator.html',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}



cookies_master = {
'ak_bmsc': 'EE8312C3CDF6F7E83698F07282335CF1~000000000000000000000000000000~YAAQbv1zPs+cRsqKAQAAa8m20BURNYZzurWoNuJgDXKrEw1FuQ2yuZUcCFYyn6pz2HjHi/NC+9U/KHviV2m5QQw+WbqYjea3VMc3aEPAd+RDd4PzmY0ChW8yicJ0tjHKOfKyNEOr0iBEBOSydeQCZ4u/PqOKXVITkbB9fdYAS4lHzEehLKEdWgh6ZsNQL0tb3H6m2k3NGdo01mO8enFjJL3XbLJrzB/QtXm7Z7w/4s9035fz6/y4S1PinfFoDdL3dLeQBNtmeDQwuJ6bU1g8pm5MnrrfZEMMRrj2SwJXYcYQywac2KlE94NxsdpdBQYQ7Lw0mrXcZf5a1DSb5GOSg3KFJRqNX3fHdhqkvnE+sXm14qKeE0f3Q9u69rEis+IHZtq1jaD6iobJ8ar6IA==',
'bm_sz': '4264B35F44AB1826613A242CE5031F1E~YAAQbv1zPtCcRsqKAQAAa8m20BVJ3qcMF0yC/+0GVGDaqv08FFKApXv9ZcGIeW7R8lLL1m0ULCd5HKBa6UYuvVorVqu4o96bMCilXE3+dKIdthlXo88tjdmTimeygJOR22SLt/PpYcBbuMk0KCTO5QM3PTEaotzujldFvg3L3NgE19EHbWZqFK6O3ANbP0nGzK7GYPvUnibq/iR960b0e0gH31E6BEkfQmisza3SRGUQyOIp/r9qExP7ECXOaEgUGz2Uaz8Zn55+7ikMBG+9Xj+H/iwkTFVeiSR01QyZacWMUx3j24Q=~3555632~3356725',
'_abck': '0D293B74E56301E541E8339FA3522E35~0~YAAQbv1zPgOdRsqKAQAAwNK20AoU59WBRrHLb0vF7oiKu4Yax+H64NKf6eykIw2AJ7qZPi3jq6fToMpeK6axDrD5YX6LNTfZNKGSvjAmry5OjGiKOHqL09Ryk92JxhHVxbRq658NAnLnXNBn6XHCKhnMYtGgaMek3II26LAcdIl585GMAwdYy4+O418hGEZ9Bt5SSxgoKg3rNcn+Bh0y+3HMFrdI9VyFmSlczZdQdUiBACr+XM15T4mpVwZz246VtM6blzbHvWPYaKAYRh6oeHHTqetJINm7UCs0DEF0JxII7cZZ3/lnklwR1yQ6XrA4rKwahp21Eaf03bFbYVK1LIECdLA7MKJq+utKi96KmAJwMfoTPzGxcVj45PctosqUsqhCCctyL9UfmD8SC9OpqGacptt6XZ0HSPrz~-1~||-1||~-1',
'OptanonAlertBoxClosed': '2023-09-26T08:59:21.629Z',
'_dyid': '-4413527388314231453',
'_dyjsession': 'f3a87fc87e8cdcfd7c620a0a2249f278',
'_dy_csc_ses': 't',
'dy_fs_page': 'www.mastercard.us%2Fen-us%2Fpersonal%2Fget-support%2Fconvert-currency.html',
'_dy_toffset': '0',
'_dyfs': '1695718755714',
'_dy_df_geo': 'Russia..Novosibirsk',
'_dy_geo': 'RU.EU.RU_NVS.RU_NVS_Novosibirsk',
'_dycnst': 'dg',
'_dyid_server': '-4413527388314231453',
'AMCVS_919F3704532951060A490D44%40AdobeOrg': '1',
'AMCV_919F3704532951060A490D44%40AdobeOrg': '179643557%7CMCMID%7C32263353963733870653984271538720900052%7CMCAAMLH-1696323562%7C6%7CMCAAMB-1696323562%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1695725962s%7CNONE%7CvVersion%7C5.5.0',
's_vnum': '1727254762522%26vn%3D1',
's_invisit': 'true',
's_cc': 'true',
'_dy_c_exps': '',
's_inv': '4702',
'visitor_id163061': '787765552',
'visitor_id163061-hash': '817bd288ca342ec0cf1b9f001bfb36a1bcb9e7d46f46665dae3cbdc42c1673c5678e03a9023294f5ff3d530e99fbca7f68f5c888',
'_dy_ses_load_seq': '14790%3A1695723516796',
'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Sep+26+2023+17%3A18%3A37+GMT%2B0700+(%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202305.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=13965c69-39fe-4541-b566-7bac9df95aec&interactionCount=1&landingPath=NotLandingPage&groups=C015%3A1%2CC016%3A1%2CC032%3A1%2CC040%3A1%2CC044%3A1%2CC049%3A1%2CC079%3A1%2CC0001%3A1%2CC006%3A1%2CC073%3A1%2CC0002%3A1%2CC025%3A1%2CC035%3A1%2CC0003%3A1%2CC011%3A1%2CC020%3A1%2CC0004%3A1&geolocation=RU%3BNVS&AwaitingReconsent=false',
'_dy_lu_ses': 'f3a87fc87e8cdcfd7c620a0a2249f278%3A1695723517352',
'_dycst': 'dk.w.c.ss.',
'bm_sv': '15D29F6BD9020C30A81561E397F9E873~YAAQbv1zPjJeScqKAQAAMXf/0BUvZUBhdggfneJjePuhW9F1a7PWMZa/FiCHzENLvUHqeXY4WYXqcIwC3X0w/hWWzDDPydC5yBZTwMAQTXUiu0fVUrw+wxBmycRAn79CgXfdNpE2Zvc3V9CMHPzcuAeqWn3+j5GGkZcCqL5KWQTBR+/3eDVcKUy7FLNnXqQVPDNqMSnYZCBg2hq/w+TFqcloBQIxJnO/9qlMNgAftEWvJmhyuD4cXfRiXJveiWpmj3T9~1',
'BIGipServerwww.dm.mc.global-https-pool': '!Jf4oUo9nk5ldUlFraRlb4PvYk2ys4l5lAA9iEFXgtqnkzMpuYTu0zwWWe8uO8fPvlWb1daHAtspmhf0=',
'TS013559a7': '01772feb4bc196b3bc2aa36cdf4bd718a6d73eaa72105b8c7e1e7cb5bf79fbdc4bf312f8110276da5a1092666ab0665c7cacc63331',
's_plt': '0.88',
's_pltp': 'en-us%3Aconvert-currency',
's_tp': '2584',
's_ips': '747.6000000238419',
's_ppv': 'en-us%253Aconvert-currency%2C44%2C29%2C1146%2C1%2C3',
's_sq': 'masterc604%252Cmastercglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253Den-us%25253Aconvert-currency%2526link%253DKAZAKHSTAN%252520TENGE%252520-%252520KZT%2526region%253DmczRowD%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Den-us%25253Aconvert-currency%2526pidt%253D1%2526oid%253Djavascript%25253Avoid%2525280%252529%2526ot%253DA',
's_tslv': '1695723531889',
's_nr30': '1695723531890-Repeat',
}

headers_master = {
    'authority': 'www.mastercard.us',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
    # 'cookie': 'ak_bmsc=EE8312C3CDF6F7E83698F07282335CF1~000000000000000000000000000000~YAAQbv1zPs+cRsqKAQAAa8m20BURNYZzurWoNuJgDXKrEw1FuQ2yuZUcCFYyn6pz2HjHi/NC+9U/KHviV2m5QQw+WbqYjea3VMc3aEPAd+RDd4PzmY0ChW8yicJ0tjHKOfKyNEOr0iBEBOSydeQCZ4u/PqOKXVITkbB9fdYAS4lHzEehLKEdWgh6ZsNQL0tb3H6m2k3NGdo01mO8enFjJL3XbLJrzB/QtXm7Z7w/4s9035fz6/y4S1PinfFoDdL3dLeQBNtmeDQwuJ6bU1g8pm5MnrrfZEMMRrj2SwJXYcYQywac2KlE94NxsdpdBQYQ7Lw0mrXcZf5a1DSb5GOSg3KFJRqNX3fHdhqkvnE+sXm14qKeE0f3Q9u69rEis+IHZtq1jaD6iobJ8ar6IA==; bm_sz=4264B35F44AB1826613A242CE5031F1E~YAAQbv1zPtCcRsqKAQAAa8m20BVJ3qcMF0yC/+0GVGDaqv08FFKApXv9ZcGIeW7R8lLL1m0ULCd5HKBa6UYuvVorVqu4o96bMCilXE3+dKIdthlXo88tjdmTimeygJOR22SLt/PpYcBbuMk0KCTO5QM3PTEaotzujldFvg3L3NgE19EHbWZqFK6O3ANbP0nGzK7GYPvUnibq/iR960b0e0gH31E6BEkfQmisza3SRGUQyOIp/r9qExP7ECXOaEgUGz2Uaz8Zn55+7ikMBG+9Xj+H/iwkTFVeiSR01QyZacWMUx3j24Q=~3555632~3356725; _abck=0D293B74E56301E541E8339FA3522E35~0~YAAQbv1zPgOdRsqKAQAAwNK20AoU59WBRrHLb0vF7oiKu4Yax+H64NKf6eykIw2AJ7qZPi3jq6fToMpeK6axDrD5YX6LNTfZNKGSvjAmry5OjGiKOHqL09Ryk92JxhHVxbRq658NAnLnXNBn6XHCKhnMYtGgaMek3II26LAcdIl585GMAwdYy4+O418hGEZ9Bt5SSxgoKg3rNcn+Bh0y+3HMFrdI9VyFmSlczZdQdUiBACr+XM15T4mpVwZz246VtM6blzbHvWPYaKAYRh6oeHHTqetJINm7UCs0DEF0JxII7cZZ3/lnklwR1yQ6XrA4rKwahp21Eaf03bFbYVK1LIECdLA7MKJq+utKi96KmAJwMfoTPzGxcVj45PctosqUsqhCCctyL9UfmD8SC9OpqGacptt6XZ0HSPrz~-1~||-1||~-1; OptanonAlertBoxClosed=2023-09-26T08:59:21.629Z; _dyid=-4413527388314231453; _dyjsession=f3a87fc87e8cdcfd7c620a0a2249f278; _dy_csc_ses=t; dy_fs_page=www.mastercard.us%2Fen-us%2Fpersonal%2Fget-support%2Fconvert-currency.html; _dy_toffset=0; _dyfs=1695718755714; _dy_df_geo=Russia..Novosibirsk; _dy_geo=RU.EU.RU_NVS.RU_NVS_Novosibirsk; _dycnst=dg; _dyid_server=-4413527388314231453; AMCVS_919F3704532951060A490D44%40AdobeOrg=1; AMCV_919F3704532951060A490D44%40AdobeOrg=179643557%7CMCMID%7C32263353963733870653984271538720900052%7CMCAAMLH-1696323562%7C6%7CMCAAMB-1696323562%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1695725962s%7CNONE%7CvVersion%7C5.5.0; s_vnum=1727254762522%26vn%3D1; s_invisit=true; s_cc=true; _dy_c_exps=; s_inv=4702; visitor_id163061=787765552; visitor_id163061-hash=817bd288ca342ec0cf1b9f001bfb36a1bcb9e7d46f46665dae3cbdc42c1673c5678e03a9023294f5ff3d530e99fbca7f68f5c888; _dy_ses_load_seq=14790%3A1695723516796; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Sep+26+2023+17%3A18%3A37+GMT%2B0700+(%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202305.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=13965c69-39fe-4541-b566-7bac9df95aec&interactionCount=1&landingPath=NotLandingPage&groups=C015%3A1%2CC016%3A1%2CC032%3A1%2CC040%3A1%2CC044%3A1%2CC049%3A1%2CC079%3A1%2CC0001%3A1%2CC006%3A1%2CC073%3A1%2CC0002%3A1%2CC025%3A1%2CC035%3A1%2CC0003%3A1%2CC011%3A1%2CC020%3A1%2CC0004%3A1&geolocation=RU%3BNVS&AwaitingReconsent=false; _dy_lu_ses=f3a87fc87e8cdcfd7c620a0a2249f278%3A1695723517352; _dycst=dk.w.c.ss.; bm_sv=15D29F6BD9020C30A81561E397F9E873~YAAQbv1zPjJeScqKAQAAMXf/0BUvZUBhdggfneJjePuhW9F1a7PWMZa/FiCHzENLvUHqeXY4WYXqcIwC3X0w/hWWzDDPydC5yBZTwMAQTXUiu0fVUrw+wxBmycRAn79CgXfdNpE2Zvc3V9CMHPzcuAeqWn3+j5GGkZcCqL5KWQTBR+/3eDVcKUy7FLNnXqQVPDNqMSnYZCBg2hq/w+TFqcloBQIxJnO/9qlMNgAftEWvJmhyuD4cXfRiXJveiWpmj3T9~1; BIGipServerwww.dm.mc.global-https-pool=!Jf4oUo9nk5ldUlFraRlb4PvYk2ys4l5lAA9iEFXgtqnkzMpuYTu0zwWWe8uO8fPvlWb1daHAtspmhf0=; TS013559a7=01772feb4bc196b3bc2aa36cdf4bd718a6d73eaa72105b8c7e1e7cb5bf79fbdc4bf312f8110276da5a1092666ab0665c7cacc63331; s_plt=0.88; s_pltp=en-us%3Aconvert-currency; s_tp=2584; s_ips=747.6000000238419; s_ppv=en-us%253Aconvert-currency%2C44%2C29%2C1146%2C1%2C3; s_sq=masterc604%252Cmastercglobal%3D%2526c.%2526a.%2526activitymap.%2526page%253Den-us%25253Aconvert-currency%2526link%253DKAZAKHSTAN%252520TENGE%252520-%252520KZT%2526region%253DmczRowD%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Den-us%25253Aconvert-currency%2526pidt%253D1%2526oid%253Djavascript%25253Avoid%2525280%252529%2526ot%253DA; s_tslv=1695723531889; s_nr30=1695723531890-Repeat',
    'referer': 'https://www.mastercard.us/en-us/personal/get-support/convert-currency.html',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
