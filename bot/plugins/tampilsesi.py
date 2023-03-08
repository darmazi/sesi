from pymongo import MongoClient
from bot import AKTIFSESI
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)

@Client.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    filters.private
)
async def tampil_sesi(_, message: Message):
    AKTIFSESI[message.chat.id] = {}
    # Membuat koneksi dengan MongoDB
    client = MongoClient("mongodb+srv://darmid:darmid@cluster0.4pdjt4g.mongodb.net/?retryWrites=true&w=majority")
    # Mengakses database dan collection
    db = client["telegram"]
    collection = db["session"]

    # Mengambil data dari collection
    result = collection.find_one()

    # Menampilkan data string sesi
    if result:
        session_string = result["session_string"]
        print("Session String:", session_string)
    else:
        print("Data tidak ditemukan")
    AKTIFSESI[message.chat.id]["TAMPIL"] = status_message
    raise message.stop_propagation()