## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgA7sBiLBNm5rv_yi5HcNCIPAd3gMCjTk1ral-GYY2M53J6m7G-ItHmzYqRToHUifvqpngdTgoelOOSHSLPAUQdFGrfBrXZGSwScqBMNqcJFCCr7xI5SO44rZl5mnNXeAKjtNXU0V6WI8sUuT1fn3zNzrHitpr09EdoOkI-fumAWmBEzFifWf4iXJ7JB_np9fYdqft_W-MQO4B7oz9ik8jwMHvclWsuWqAmbOe8Zuev-uO0sHlxsfmi7D-u1s466ta1g2SCeJMWvk0N-X6zjnx4SgxL7fZ_k8Z270bcoxy8TvWW28YzngPAMQ7tBrXH2pRmu7NkBJbhumKtl8pxswYM6AAAAATrk3zkA")
BOT_TOKEN = getenv("BOT_TOKEN", "5515817482:AAElvPoJSsjiVbmrPF7CbfYtmx2How1bpMk")
BOT_NAME = getenv("BOT_NAME", "❦︎ 𝐀.𝐑 ✹⃝‌꙰🇪🇬 𝐌.𝐀.𝐗.𝐃.𝐄.𝐕.𝐋⸙ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ")
API_ID = int(getenv("API_ID", "10157898"))
API_HASH = getenv("API_HASH", "33f9a8b3d0aec401fbe54a2019e7df62")
OWNER_NAME = getenv("OWNER_NAME", "⋆ ⃝➼𝐌𝐀𝐗 𝐃𝐄𝐕𝑳 ꗛ❤")
OWNER_USERNAME = getenv("OWNER_USERNAME", "RTP_M_A_X")
ALIVE_NAME = getenv("ALIVE_NAME", "⋆ ⃝➼𝐌𝐀𝐗 𝐃𝐄𝐕𝑳 ꗛ❤")
BOT_USERNAME = getenv("BOT_USERNAME", "M_A_X_6_BOT")
OWNER_ID = getenv("OWNER_ID", "1991857319")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "RT_P_M_A_X")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "M_A_X_DEVL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","R_T_P_M_A_X")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
