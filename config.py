# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
 Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.

.youtube.com	TRUE	/	TRUE	1752461501	GPS	1
.youtube.com	TRUE	/	TRUE	0	YSC	Jc39_5U6nps
.youtube.com	TRUE	/	TRUE	1768012034	__Secure-ROLLOUT_TOKEN	CO_GwoWW8qq0QhD5wOePpbuOAxiR9NmupruOAw%3D%3D
.youtube.com	TRUE	/	TRUE	1768012034	VISITOR_INFO1_LIVE	VFFDMplu99M
.youtube.com	TRUE	/	TRUE	1768012034	VISITOR_PRIVACY_METADATA	CgJJThIEGgAgPQ%3D%3D
.youtube.com	TRUE	/	TRUE	1787020035	PREF	tz=Asia.Kolkata
.youtube.com	TRUE	/	TRUE	1783996033	__Secure-1PSIDTS	sidts-CjEB5H03P4DYlhgDleH16CxK1lgbRCe9On8NwKvx8WlHpa2Z93y-TkGcJo9bavKXRHcqEAA
.youtube.com	TRUE	/	TRUE	1783996033	__Secure-3PSIDTS	sidts-CjEB5H03P4DYlhgDleH16CxK1lgbRCe9On8NwKvx8WlHpa2Z93y-TkGcJo9bavKXRHcqEAA
.youtube.com	TRUE	/	FALSE	1787020033	HSID	AM2y8nuQHSZE41DRr
.youtube.com	TRUE	/	TRUE	1787020033	SSID	ArWN56zWY8lh79pY7
.youtube.com	TRUE	/	FALSE	1787020033	APISID	TXcDe_SwcQp0SEu_/AdCYZ2-lSa3TAaYlr
.youtube.com	TRUE	/	TRUE	1787020033	SAPISID	-PLDlrSrgxdeSYjo/AWASvokFPbX0l5qge
.youtube.com	TRUE	/	TRUE	1787020033	__Secure-1PAPISID	-PLDlrSrgxdeSYjo/AWASvokFPbX0l5qge
.youtube.com	TRUE	/	TRUE	1787020033	__Secure-3PAPISID	-PLDlrSrgxdeSYjo/AWASvokFPbX0l5qge
.youtube.com	TRUE	/	FALSE	1787020033	SID	g.a000zAjbrgC867l3yjw8105TrIhYgGgFDTOmsGPJIGaScyZr0Kf-jLjdrZDR9g2zYXaSDhxtzAACgYKAbASARQSFQHGX2MimLrQQ-Zxaz7VX76oVLpaYxoVAUF8yKoFham6yiZo7-CTVg4ynaUm0076
.youtube.com	TRUE	/	TRUE	1787020033	__Secure-1PSID	g.a000zAjbrgC867l3yjw8105TrIhYgGgFDTOmsGPJIGaScyZr0Kf-zPS6asZWLkTkchD_QV7w_QACgYKAbUSARQSFQHGX2MiPFVVzJh04vyLXYt7QuBkchoVAUF8yKoupVerrlijm9MsqtOVZoma0076
.youtube.com	TRUE	/	TRUE	1787020033	__Secure-3PSID	g.a000zAjbrgC867l3yjw8105TrIhYgGgFDTOmsGPJIGaScyZr0Kf-KxzUOZgqMD3GtbAikCKyOgACgYKARQSARQSFQHGX2Mi7IoaeYSiZr8MqTcJr0SGiBoVAUF8yKq_rbo9XQJL8CqBoWZoWDeR0076
.youtube.com	TRUE	/	FALSE	1783996037	SIDCC	AKEyXzXYw3jb5AKt-2fl1LGmaoqwSDOH87A55IaKWp47-ZS-vyRGwxjTfvtOACR0LdhNQV29zw
.youtube.com	TRUE	/	TRUE	1783996037	__Secure-1PSIDCC	AKEyXzXjwH_L2KZS6usVbB7QnveZ3p32vh7PFZ3IYa8v9BcrbEtcol_ovBqmHPnpoyxQPcg
.youtube.com	TRUE	/	TRUE	1783996037	__Secure-3PSIDCC	AKEyXzULsbN-k7EIlsHPDXoXAfGd7wg-GGqJ2d9G-UPLKGa1cbCmJEgZeuM0O-0JDUXvGgVpog
.youtube.com	TRUE	/	TRUE	1787020034	LOGIN_INFO	AFmmF2swRQIgXI-VQ7OgiCPAl0-Rw-HksqzbqCEqIedgN-ES9I3KbyoCIQCg1Ne7T4RqU27t-UtIPjf6ZSAS1eBMGi5J4Phv4_0REg:QUQ3MjNmd1p4SmhSalRtVTFzRUVwQk1ZVmI4NHQtOEpxNHV2emJ5eHIwUmJPVkYxV2JsVVpjRjM4MDZIXzN3TzgzUExvSDA0TjV3T01mOTRTeW5mVHRvZGFpdzVZZkxtVUdsM2xRUDZoRDhrSThJSFpvVV93dk84UDBDY1ROaWptQTdBUjNacjE2R3pnZHJRQ3hLVVVRaVJxaTY4REpqVmFB
.youtube.com	TRUE	/	FALSE	1752460047	ST-1z0qytu	csn=V8w25asx6M6fxngO&itct=CH8Qh_YEGAMiEwja5uyupruOAxWVSl4EHSa-Dy5aD0ZFd2hhdF90b193YXRjaJoBBQgkEI4e
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
