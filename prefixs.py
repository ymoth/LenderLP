
import json
with open('config.json', encoding="utf-8") as RP:
    config = json.load(RP)

p = config['prefix']
sticker = config['stickerLP'] + " | "
error_sticker = config['errorSticker'] + " | "

stickerforstart = config['stickerLP']

error_stickerforstart = config['errorSticker']

