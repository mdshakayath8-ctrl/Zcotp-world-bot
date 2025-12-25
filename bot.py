from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ===== MUST SET =====
TOKEN = "8094096874:AAF3o_CN9woDcv3ARZoPXFD6lBSWKyYjjG4"     # BotFather token এখানে বসাও
ADMIN_ID = 7833093821              # numeric Telegram ID এখানে বসাও
# ===================

user_menu = ReplyKeyboardMarkup(
    [
        ["📞 Get Number", "🌍 Choose Country"],
        ["🔁 Change Number", "🌐 Change Country"],
        ["🔐 Get OTP"],
        ["🆘 Support"]
    ],
    resize_keyboard=True
)

admin_menu = ReplyKeyboardMarkup(
    [
        ["➕ Add Number", "🌍 Add Country"],
        ["📋 View Users"],
        ["🆘 Support"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if uid == ADMIN_ID:
        await update.message.reply_text("👑 Admin Panel", reply_markup=admin_menu)
    else:
        await update.message.reply_text("👤 User Panel", reply_markup=user_menu)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = update.message.text

    if t == "📞 Get Number":
        await update.message.reply_text("📞 Demo number assigned")
    elif t == "🌍 Choose Country":
        await update.message.reply_text("🌍 Country selected")
    elif t == "🔁 Change Number":
        await update.message.reply_text("🔁 Number changed")
    elif t == "🌐 Change Country":
        await update.message.reply_text("🌐 Country changed")
    elif t == "🔐 Get OTP":
        await update.message.reply_text("🔐 OTP (demo)")
    elif t == "🆘 Support":
        await update.message.reply_text("🆘 Contact admin")
    elif t == "➕ Add Number":
        await update.message.reply_text("➕ Admin: add number")
    elif t == "🌍 Add Country":
        await update.message.reply_text("🌍 Admin: add country")
    elif t == "📋 View Users":
        await update.message.reply_text("📋 Admin: users list")
    else:
        await update.message.reply_text("❓ Unknown option")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling()
