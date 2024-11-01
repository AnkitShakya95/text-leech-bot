import os

API_ID    = os.environ.get("API_ID", "221006955")
API_HASH  = os.environ.get("API_HASH", "0e8f93300ccbbcd56066e6d790b0d3b2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7830905185:AAECMKpAs_jVD3bF3p-obLiK6rMDvw3O0cw") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
