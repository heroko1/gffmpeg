#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1169977435
    OWNER = config("OWNER")
    ffmpegcode = ["-metadata title=" One Piece encoded by @onepieceseries" -map 0:v -map 0:a -b:a 192k -c:a aac -c:v libx265 -color_primaries 1 -color_range 1 -color_trc 1 -colorspace 1 -crf 24.2 -map 0:s? -pix_fmt yuv420p -preset slow -profile:v main -vf smartblur=1.5:-0.35:-3.5:0.65:0.25:2.0,scale=1920:1080:spline16+accurate_rnd+full_chroma_int -x265-params me=2:rd=4:subme=7:aq-mode=3:aq-strength=1:deblock=1,1:psy-rd=1:psy-rdoq=1:rdoq-level=2:merange=57:bframes=8:b-adapt=2:limit-sao=1:frame-threads=3:no-info=1"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/18b4993d3f1e169479caf.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
