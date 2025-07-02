# # from telegram import Update
# # from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# # import random
# # import datetime

# # TELEGRAM_TOKEN = "7800118937:AAFrsLwwxvqYy3GmvLgU8MGzt_AxtVBlyfk"

# # # # Օգտատերերի տվյալները պահելու dictionary
# # # users_data = {}
# # # # Օրվա հաղթողների ցուցակ
# # # winners_today = []

# # # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     user_id = update.message.from_user.id
# # #     users_data[user_id] = {
# # #         "target": random.randint(1, 100),
# # #         "attempts_left": 5,
# # #         "paid": False,
# # #         "username": update.message.from_user.username or str(user_id)
# # #     }
# # #     await update.message.reply_text(
# # #         "Բարև 👋\n"
# # #         "Ես թիվ գուշակող խաղային բոտ եմ!\n"
# # #         "Ես մտածել եմ 1-100 միջակայքում թիվ։ Գուշակիր այն։\n"
# # #         "Ունեք 5 անվճար փորձ։\n"
# # #         "Վճարելով 1000֏՝ կստանաք 20 փորձ։\n"
# # #         "Վճարելու համար՝ IDRAM` 077779321 📲\n"
# # #         "Վճարումից հետո գրիր՝ @aleqsmirakyan"
# # #     )

# # # async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     user_id = update.message.from_user.id
# # #     if user_id not in users_data:
# # #         await update.message.reply_text("Սկսելու համար գրիր /start")
# # #         return

# # #     try:
# # #         guess = int(update.message.text)
# # #     except ValueError:
# # #         await update.message.reply_text("Խնդրում եմ մուտքագրիր ամբողջ թիվ։")
# # #         return

# # #     data = users_data[user_id]
# # #     if data["attempts_left"] <= 0:
# # #         await update.message.reply_text(
# # #             "Փորձերդ ավարտվել են ❌\n"
# # #             "Վճարիր 1000֏՝ 077779321-ին՝ 20 փորձ ստանալու համար։"
# # #         )
# # #         return

# # #     data["attempts_left"] -= 1
# # #     target = data["target"]

# # #     if guess == target:
# # #         winners_today.append(data["username"])
# # #         await update.message.reply_text("🎉 Շնորհավորում եմ! Դու ճիշտ գուշակեցիր թիվը!")
# # #         data["target"] = random.randint(1, 100)
# # #         data["attempts_left"] = 5 if not data["paid"] else 20
# # #     elif guess < target:
# # #         await update.message.reply_text(f"📉 Ավելի բարձր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")
# # #     else:
# # #         await update.message.reply_text(f"📈 Ավելի ցածր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")

# # # async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     await update.message.reply_text("✏️ Մուտքագրիր թիվ (օր.՝ 45) կամ գրիր /start նոր խաղ սկսելու համար։")

# # # async def winners(update: Update, context: ContextTypes.DEFAULT_TYPE):
# # #     today = datetime.datetime.now().strftime("%Y-%m-%d")
# # #     if winners_today:
# # #         text = f"🏆 {today} օրվա հաղթող(ներ)ն են՝\n" + "\n".join(winners_today)
# # #     else:
# # #         text = "Այսօր դեռ հաղթող չկա։"
# # #     await update.message.reply_text(text)

# # # app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
# # # app.add_handler(CommandHandler("start", start))
# # # app.add_handler(CommandHandler("help", help_command))
# # # app.add_handler(CommandHandler("winners", winners))
# # # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess))

# # # print("Բոտը ակտիվ է ✅")
# # # app.run_polling()

# # ADMIN_ID = 7967129348
# # # Օգտատերերի տվյալները պահելու dictionary
# # users_data = {}
# # pending_verifications = {}  # Նրանք, ովքեր գրել են "վճարել եմ"

# # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.message.from_user.id

# #     users_data[user_id] = {
# #         "target": random.randint(1, 100),
# #         "attempts_left": 5,
# #         "paid": False
# #     }

# #     await update.message.reply_text(
# #         "Բարև 👋\n"
# #         "Ես թիվ գուշակող խաղային բոտ եմ!\n"
# #         "Ես մտածել եմ 1-100 միջակայքում թիվ։ Գուշակիր այն։\n"
# #         "Ունեք 5 անվճար փորձ։\n"
# #         "Վճարելով 1000֏՝ կստանաք 20 փորձ։\n"
# #         "Վճարելու համար՝ IDRAM՝ 077779321 📲\n"
# #         "Վճարելուց հետո գրիր՝ «վճարել եմ»։"
# #     )

# # async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     await update.message.reply_text("✏️ Մուտքագրիր թիվ (օր.՝ 45) կամ գրիր /start նոր խաղ սկսելու համար։")

# # async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     user_id = update.message.from_user.id
# #     text = update.message.text.lower()

# #     # Եթե ադմինն է և ուզում է հաստատել վճարումը
# #     if text.startswith("/approve_"):
# #         if user_id != ADMIN_ID:
# #             await update.message.reply_text("❌ Դուք իրավունք չունեք այս գործողությունն անել։")
# #             return
# #         try:
# #             approved_id = int(text.split("_")[1])
# #             if approved_id in users_data:
# #                 users_data[approved_id]["paid"] = True
# #                 users_data[approved_id]["attempts_left"] += 20

# #                 await context.bot.send_message(chat_id=approved_id,
# #                     text="✅ Ձեր վճարումը հաստատվել է։ Դուք ստացել եք 20 նոր փորձ։ Խաղը շարունակեք։")

# #                 await update.message.reply_text(f"✅ {pending_verifications.get(approved_id, '')}-ի հարցումը հաստատվեց։")
# #                 pending_verifications.pop(approved_id, None)
# #             else:
# #                 await update.message.reply_text("❌ Այդ օգտատերը սկսած խաղ չունի։")
# #         except Exception:
# #             await update.message.reply_text("⚠️ Սխալ ID կամ հրաման։")
# #         return

# #     # Եթե օգտատերը գրել է "վճարել եմ"
# #     if "վճարել եմ" in text:
# #         pending_verifications[user_id] = update.message.from_user.full_name
# #         await update.message.reply_text("✅ Ձեր հարցումը փոխանցվել է ադմինին հաստատման։")

# #         await context.bot.send_message(
# #             chat_id=ADMIN_ID,
# #             text=f"💸 {pending_verifications[user_id]} գրել է 'վճարել եմ':\nՀաստատե՞լ՝ /approve_{user_id}"
# #         )
# #         return

# #     # Եթե օգտատերը խաղում է՝ փորձելով գուշակել թիվ
# #     if user_id not in users_data:
# #         await update.message.reply_text("Սկսելու համար գրիր /start")
# #         return

# #     try:
# #         guess = int(update.message.text)
# #     except ValueError:
# #         await update.message.reply_text("Խնդրում եմ մուտքագրիր ամբողջ թիվ։")
# #         return

# #     data = users_data[user_id]
# #     if data["attempts_left"] <= 0:
# #         await update.message.reply_text(
# #             "Փորձերդ ավարտվել են ❌\n"
# #             "Վճարիր 1000֏՝ 077779321-ին՝ 20 նոր փորձ ստանալու համար։"
# #         )
# #         return

# #     data["attempts_left"] -= 1
# #     target = data["target"]

# #     if guess == target:
# #         await update.message.reply_text("🎉 Շնորհավորում եմ! Դու ճիշտ գուշակեցիր թիվը!")
# #         data["target"] = random.randint(1, 100)
# #         data["attempts_left"] = 5 if not data["paid"] else 20
# #     elif guess < target:
# #         await update.message.reply_text(f"📉 Ավելի բարձր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")
# #     else:
# #         await update.message.reply_text(f"📈 Ավելի ցածր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")

# # app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# # app.add_handler(CommandHandler("start", start))
# # app.add_handler(CommandHandler("help", help_command))
# # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# # print("Բոտը ակտիվ է ✅")
# # app.run_polling()



# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import random

# TELEGRAM_TOKEN = "7800118937:AAFrsLwwxvqYy3GmvLgU8MGzt_AxtVBlyfk"

# ADMIN_ID = 7967129348  # Փոխիր քո Telegram ID-ով

# # Օգտատերերի տվյալները պահելու dictionary
# users_data = {}
# pending_verifications = {}  # Նրանք, ովքեր գրել են "վճարել եմ"

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id

#     users_data[user_id] = {
#         "target": random.randint(1, 100),
#         "attempts_left": 5,
#         "paid": False
#     }

#     await update.message.reply_text(
#         "Բարև 👋\n"
#         "Ես թիվ գուշակող խաղային բոտ եմ!\n"
#         "Ես մտածել եմ 1-100 միջակայքում թիվ։ Գուշակիր այն։\n"
#         "Ունեք 5 անվճար փորձ։\n"
#         "Վճարելով 1000֏՝ կստանաք 20 փորձ։\n"
#         "Վճարելու համար՝ IDRAM՝ 077779321 📲\n"
#         "Վճարելուց հետո գրիր՝ «վճարել եմ»։"
#     )

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("✏️ Մուտքագրիր թիվ (օր.՝ 45) կամ գրիր /start նոր խաղ սկսելու համար։")

# async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.lower()

#     # 1. Ադմինի վճարման հաստատում
#     if text.startswith("/approve_"):
#         if user_id != ADMIN_ID:
#             await update.message.reply_text("❌ Դուք իրավունք չունեք այս գործողությունն անել։")
#             return
#         try:
#             approved_id = int(text.split("_")[1])
#         except:
#             await update.message.reply_text("⚠️ Սխալ ID կամ հրաման։")
#             return

#         if approved_id in users_data:
#             users_data[approved_id]["paid"] = True
#             users_data[approved_id]["attempts_left"] += 20

#             await context.bot.send_message(chat_id=approved_id,
#                 text="✅ Ձեր վճարումը հաստատվել է։ Դուք ստացել եք 20 նոր փորձ։ Խաղը շարունակեք։")

#             await update.message.reply_text(f"✅ {pending_verifications.get(approved_id, 'Օգտատեր')}-ի հարցումը հաստատվեց։")
#             pending_verifications.pop(approved_id, None)
#         else:
#             await update.message.reply_text("❌ Այդ օգտատերը սկսած խաղ չունի։")
#         return

#     # 2. Օգտատիրոջ "վճարել եմ" հաղորդագրությունը
#     if "վճարել եմ" in text:
#         pending_verifications[user_id] = update.message.from_user.full_name
#         await update.message.reply_text("✅ Ձեր հարցումը փոխանցվել է ադմինին հաստատման։")

#         await context.bot.send_message(
#             chat_id=ADMIN_ID,
#             text=f"💸 {pending_verifications[user_id]} գրել է 'վճարել եմ':\nՀաստատե՞լ՝ /approve_{user_id}"
#         )
#         return

#     # 3. Եթե օգտատերը խաղի մեջ չէ, հուշում ենք սկսել /start-ով
#     if user_id not in users_data:
#         await update.message.reply_text("Սկսելու համար գրիր /start")
#         return

#     # 4. Գուշակում ենք թիվ
#     try:
#         guess = int(text)
#     except ValueError:
#         await update.message.reply_text("Խնդրում եմ մուտքագրիր ամբողջ թիվ։")
#         return

#     data = users_data[user_id]
#     if data["attempts_left"] <= 0:
#         await update.message.reply_text(
#             "Փորձերդ ավարտվել են ❌\n"
#             "Վճարիր 1000֏՝ 077779321-ին՝ 20 նոր փորձ ստանալու համար։"
#         )
#         return

#     data["attempts_left"] -= 1
#     target = data["target"]

#     if guess == target:
#         await update.message.reply_text("🎉 Շնորհավորում եմ! Դու ճիշտ գուշակեցիր թիվը!")
#         data["target"] = random.randint(1, 100)
#         data["attempts_left"] = 5 if not data["paid"] else 20
#     elif guess < target:
#         await update.message.reply_text(f"📉 Ավելի բարձր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")
#     else:
#         await update.message.reply_text(f"📈 Ավելի ցածր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")

# app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("help", help_command))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# print("Բոտը ակտիվ է ✅")
# app.run_polling()


# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import random

# # 🤖 Քո բոտի token-ը
# TELEGRAM_TOKEN = "7800118937:AAFrsLwwxvqYy3GmvLgU8MGzt_AxtVBlyfk"

# # 👑 Ադմինի Telegram ID-ն (ձերը)
# ADMIN_ID = 7967129348

# # 📊 Օգտատերերի տվյալների պահոց
# users_data = {}
# pending_verifications = {}  # Նրանք, ովքեր գրել են "վճարել եմ" կամ "վճարված է"

# # 🚀 Սկսել խաղը
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id

#     users_data[user_id] = {
#         "target": random.randint(1, 100),
#         "attempts_left": 5,
#         "paid": False
#     }

#     await update.message.reply_text(
#         "Բարև 👋\n"
#         "Ես թիվ գուշակող խաղային բոտ եմ!\n"
#         "Ես մտածել եմ 1-100 միջակայքում թիվ։ Գուշակիր այն։\n"
#         "Ունեք 5 անվճար փորձ։\n"
#         "Վճարելով 1000֏՝ կստանաք 20 փորձ։\n"
#         "Վճարելու համար՝ IDRAM՝ 077779321 📲\n"
#         "Վճարումից հետո գրիր՝ «վճարել եմ» կամ «վճարված է»։"
#     )

# # ℹ️ Օգնություն
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("✏️ Մուտքագրիր թիվ (օր.՝ 45) կամ գրիր /start նոր խաղ սկսելու համար։")

# # 🧠 Հաղորդագրությունների գլխավոր մշակիչ
# async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.lower().strip()

#     # ✅ Վճարման հաստատում ադմինի կողմից
#     if text.startswith("/approve_"):
#         if user_id != ADMIN_ID:
#             await update.message.reply_text("❌ Դուք իրավունք չունեք այս գործողությունն անել։")
#             return
#         try:
#             approved_id = int(text.split("_")[1])
#         except:
#             await update.message.reply_text("⚠️ Սխալ ID կամ հրաման։")
#             return

#         if approved_id in users_data:
#             users_data[approved_id]["paid"] = True
#             users_data[approved_id]["attempts_left"] += 20

#             await context.bot.send_message(chat_id=approved_id,
#                 text="✅ Ձեր վճարումը հաստատվել է։ Դուք ստացել եք 20 նոր փորձ։ Խաղը շարունակեք։")

#             await update.message.reply_text(f"✅ {pending_verifications.get(approved_id, 'Օգտատեր')}-ի հարցումը հաստատվեց։")
#             pending_verifications.pop(approved_id, None)
#         else:
#             await update.message.reply_text("❌ Այդ օգտատերը սկսած խաղ չունի։")
#         return

#     # 💸 Օգտատիրոջ "վճարել եմ" կամ "վճարված է" հաղորդագրությունը
#     if "վճարել եմ" in text or "վճարված է" in text:
#         pending_verifications[user_id] = update.message.from_user.full_name
#         await update.message.reply_text(
#             "✅ Ձեր հարցումը փոխանցվել է ադմինին հաստատման։\n"
#             "Ադմինին պետք է ուղարկի հետևյալ հրամանը՝ \n"
#             f"/approve_{user_id} \n"
#             "Այս հրամանը պետք է գրի Telegram-ում բոտի հետ չատում։"
#         )

#         await context.bot.send_message(
#             chat_id=ADMIN_ID,
#             text=f"💸 {pending_verifications[user_id]} գրել է '{update.message.text}':\nՀաստատե՞լ՝ /approve_{user_id}"
#         )
#         return

#     # 🔁 Եթե խաղը սկսված չէ՝ հուշում տալ
#     if user_id not in users_data:
#         await update.message.reply_text("Սկսելու համար գրիր /start")
#         return

#     # 🔢 Թվի գուշակում
#     try:
#         guess = int(text)
#     except ValueError:
#         await update.message.reply_text("Խնդրում եմ մուտքագրիր ամբողջ թիվ։")
#         return

#     data = users_data[user_id]
#     if data["attempts_left"] <= 0:
#         await update.message.reply_text(
#             "Փորձերդ ավարտվել են ❌\n"
#             "Վճարիր 1000֏՝ 077779321-ին՝ 20 նոր փորձ ստանալու համար։"
#         )
#         return

#     data["attempts_left"] -= 1
#     target = data["target"]

#     if guess == target:
#         await update.message.reply_text("🎉 Շնորհավորում եմ! Դու ճիշտ գուշակեցիր թիվը!")
#         data["target"] = random.randint(1, 100)
#         data["attempts_left"] = 5 if not data["paid"] else 20
#     elif guess < target:
#         await update.message.reply_text(f"📉 Ավելի բարձր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")
#     else:
#         await update.message.reply_text(f"📈 Ավելի ցածր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")

# # ✅ Բոտի գործարկում
# app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("help", help_command))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

# print("Բոտը ակտիվ է ✅")
# app.run_polling()


# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
# import random

# # 🔐 Token & Admin
# TELEGRAM_TOKEN = "7800118937:AAFrsLwwxvqYy3GmvLgU8MGzt_AxtVBlyfk"
# ADMIN_ID = 7967129348  # փոխիր քո ID-ով

# # 📊 Տվյալներ
# users_data = {}
# pending_verifications = {}

# # 🚀 /start հրաման
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id

#     users_data[user_id] = {
#         "target": random.randint(1, 100),
#         "attempts_left": 5,
#         "paid": False
#     }

#     await update.message.reply_text(
#         "Բարև 👋\n"
#         "Ես թիվ գուշակող խաղային բոտ եմ!\n"
#         "Ես մտածել եմ 1-100 միջակայքում թիվ։ Գուշակիր այն։\n"
#         "Ունեք 5 անվճար փորձ։\n"
#         "Վճարելով 1000֏՝ կստանաք 20 փորձ։\n"
#         "Վճարելու համար՝ IDRAM՝ 077779321 📲\n"
#         "Վճարումից հետո գրիր՝ «վճարել եմ»։"
#     )

# # ℹ️ /help հրաման
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("✏️ Մուտքագրիր թիվ (օր.՝ 45) կամ գրիր /start նոր խաղ սկսելու համար։")

# # 🧠 Գլխավոր հաղորդագրությունների մշակիչ
# async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.lower().strip()

#     # ✅ Վճարել եմ
#     if "վճարել եմ" in text or "վճարված է" in text:
#         pending_verifications[user_id] = update.message.from_user.full_name
#         await update.message.reply_text("✅ Ձեր հարցումը փոխանցվել է ադմինին հաստատման։")

#         # Հաստատման կոճակ
#         keyboard = InlineKeyboardMarkup([
#             [InlineKeyboardButton("✅ Հաստատել վճարումը", callback_data=f"approve_{user_id}")]
#         ])

#         await context.bot.send_message(
#             chat_id=ADMIN_ID,
#             text=f"💸 {pending_verifications[user_id]} գրել է «{update.message.text}»։",
#             reply_markup=keyboard
#         )
#         return

#     # 👤 Սկսած չէ
#     if user_id not in users_data:
#         await update.message.reply_text("Սկսելու համար գրիր /start")
#         return

#     # 🔢 Թվի գուշակում
#     try:
#         guess = int(text)
#     except ValueError:
#         await update.message.reply_text("Խնդրում եմ մուտքագրիր ամբողջ թիվ։")
#         return

#     data = users_data[user_id]
#     if data["attempts_left"] <= 0:
#         await update.message.reply_text(
#             "Փորձերդ ավարտվել են ❌\n"
#             "Վճարիր 1000֏՝ 077779321-ին՝ 20 նոր փորձ ստանալու համար։"
#         )
#         return

#     data["attempts_left"] -= 1
#     target = data["target"]

#     if guess == target:
#         await update.message.reply_text("🎉 Շնորհավորում եմ! Դու ճիշտ գուշակեցիր թիվը!")
#         data["target"] = random.randint(1, 100)
#         data["attempts_left"] = 5 if not data["paid"] else 20
#     elif guess < target:
#         await update.message.reply_text(f"📉 Ավելի բարձր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")
#     else:
#         await update.message.reply_text(f"📈 Ավելի ցածր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")

# # ✅ Կոճակով հաստատման callback
# async def approve_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()

#     if query.from_user.id != ADMIN_ID:
#         await query.edit_message_text("❌ Դուք իրավունք չունեք այս գործողությունն անել։")
#         return

#     data = query.data
#     if data.startswith("approve_"):
#         user_id = int(data.split("_")[1])
#         if user_id in users_data:
#             users_data[user_id]["paid"] = True
#             users_data[user_id]["attempts_left"] += 20

#             await context.bot.send_message(
#                 chat_id=user_id,
#                 text="✅ Ձեր վճարումը հաստատվել է։ Դուք ստացել եք 20 նոր փորձ։ Խաղը շարունակեք։"
#             )

#             await query.edit_message_text(f"✅ {pending_verifications.get(user_id, 'Օգտատեր')}-ի վճարումը հաստատվեց։")
#             pending_verifications.pop(user_id, None)
#         else:
#             await query.edit_message_text("❌ Այդ օգտատերը դեռ խաղ չի սկսել։")

# # ▶️ Գործարկում
# app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("help", help_command))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
# app.add_handler(CallbackQueryHandler(approve_callback))

# print("Բոտը ակտիվ է ✅")
# app.run_polling()


# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
# import random

# TELEGRAM_TOKEN = "7800118937:AAFrsLwwxvqYy3GmvLgU8MGzt_AxtVBlyfk"
# ADMIN_ID = 7967129348

# users_data = {}
# pending_verifications = {}

# # ✅ /start հրաման
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     users_data[user_id] = {
#         "target": random.randint(1, 100),
#         "attempts_left": 5,
#         "paid": False
#     }

#     keyboard = ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton("🎮 Սկսել խաղը"), KeyboardButton("ℹ️ Օգնություն")]
#         ],
#         resize_keyboard=True
#     )

#     await update.message.reply_text(
#         "Բարև 👋\nԵս թիվ գուշակող խաղային բոտ եմ:\nԳուշակիր 1-100 միջակայքում թիվը։\n"
#         "Ունես 5 անվճար փորձ։ Վճարելով՝ ստանում ես 20 նոր փորձ։\n"
#         "Վճարելու համար IDRAM՝ 077779321 📲\n"
#         "Վճարելուց հետո գրիր «վճարել եմ»։",
#         reply_markup=keyboard
#     )

# # ✅ /help հրաման
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("✏️ Պարզապես մուտքագրիր թիվ (օրինակ՝ 45) կամ սեղմիր 🎮 Սկսել խաղը՝ նորից սկսելու համար։")

# # ✅ Գլխավոր հաղորդագրությունների մշակիչ
# async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.message.from_user.id
#     text = update.message.text.lower().strip()

#     # 🆘 Բառային կոճակներ
#     if text == "🎮 սկսել խաղը":
#         await start(update, context)
#         return
#     elif text == "ℹ️ օգնություն":
#         await help_command(update, context)
#         return

#     # 💸 Վճարել եմ
#     if "վճարել եմ" in text or "վճարված է" in text:
#         pending_verifications[user_id] = update.message.from_user.full_name
#         await update.message.reply_text("✅ Ձեր հարցումը փոխանցվել է ադմինին հաստատման։")

#         keyboard = InlineKeyboardMarkup([
#             [InlineKeyboardButton("✅ Հաստատել", callback_data=f"approve_{user_id}"),
#              InlineKeyboardButton("❌ Չեղարկել", callback_data=f"cancel_{user_id}")]
#         ])

#         await context.bot.send_message(
#             chat_id=ADMIN_ID,
#             text=f"💸 {pending_verifications[user_id]} գրել է «{update.message.text}»:",
#             reply_markup=keyboard
#         )
#         return

#     # 🤖 Սկսած չէ
#     if user_id not in users_data:
#         await update.message.reply_text("Խնդրում եմ գրիր /start՝ խաղը սկսելու համար։")
#         return

#     # 🔢 Թվի փորձ
#     try:
#         guess = int(text)
#     except ValueError:
#         await update.message.reply_text("Խնդրում եմ մուտքագրիր ամբողջ թիվ։")
#         return

#     data = users_data[user_id]
#     if data["attempts_left"] <= 0:
#         await update.message.reply_text("Փորձերդ ավարտվել են ❌\nՎճարիր 1000֏՝ 20 նոր փորձ ստանալու համար։")
#         return

#     data["attempts_left"] -= 1
#     if guess == data["target"]:
#         await update.message.reply_text("🎉 Դու ճիշտ գուշակեցիր թիվը!\nՆոր թիվ եմ մտածում․․․")
#         data["target"] = random.randint(1, 100)
#         data["attempts_left"] = 5 if not data["paid"] else 20
#     elif guess < data["target"]:
#         await update.message.reply_text(f"📉 Ավելի բարձր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")
#     else:
#         await update.message.reply_text(f"📈 Ավելի ցածր թիվ փորձիր։ Մնացել է {data['attempts_left']} փորձ։")

# # ✅ Callback - approve / cancel
# async def approve_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     data = query.data

#     if query.from_user.id != ADMIN_ID:
#         await query.edit_message_text("❌ Դուք իրավունք չունեք այս գործողությունն անել։")
#         return

#     if data.startswith("approve_"):
#         user_id = int(data.split("_")[1])
#         if user_id in users_data:
#             users_data[user_id]["paid"] = True
#             users_data[user_id]["attempts_left"] += 20
#             await context.bot.send_message(chat_id=user_id,
#                 text="✅ Ձեր վճարումը հաստատվել է։ Ստացել եք 20 նոր փորձ։")
#             await query.edit_message_text("💰 Վճարումը հաստատվեց։")
#             pending_verifications.pop(user_id, None)
#         else:
#             await query.edit_message_text("❌ Այդ օգտատերը խաղը չի սկսել։")

#     elif data.startswith("cancel_"):
#         user_id = int(data.split("_")[1])
#         await context.bot.send_message(chat_id=user_id,
#             text="❌ Ձեր վճարումը մերժվել է ադմինի կողմից։")
#         await query.edit_message_text("🚫 Վճարումը չեղարկվեց։")
#         pending_verifications.pop(user_id, None)

# # ▶️ Bot launch
# app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("help", help_command))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
# app.add_handler(CallbackQueryHandler(approve_callback))

# print("Բոտը ակտիվ է ✅")
# app.run_polling()


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import random

TELEGRAM_TOKEN = "7800118937:AAFrsLwwxvqYy3GmvLgU8MGzt_AxtVBlyfk"
ADMIN_ID = 7967129348  # Քո Telegram ID

users_data = {}
pending_verifications = {}

# ✅ reply keyboard-ը միանգամից դնում ենք
reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🎮 Սկսել խաղը"), KeyboardButton("ℹ️ Օգնություն")]
    ],
    resize_keyboard=True
)

# ✅ /start կամ 🎮 Սկսել խաղը
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    users_data[user_id] = {
        "target": random.randint(1, 100),
        "attempts_left": 5,
        "paid": False
    }
    await update.message.reply_text(
        "Բարև 👋\nԵս թիվ գուշակող խաղային բոտ եմ։ Քեզ մաղթում եմ լավ խաղ․․․🎉🎉🎉\n",
        # "Ունեք 5 անվճար փորձ։\n",
        # "Վճարելով 1000֏՝ կստանաք 20 փորձ։\n",
        # "Վճարելու համար՝ IDRAM` 077779321 📲\n",
        # "Վճարումից հետո գրիր՝ վճարել եմ",
        reply_markup=reply_keyboard
    )

# ✅ /help կամ ℹ️ Օգնություն
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✏️ Ուղարկիր թիվ (օրինակ՝ 45) կամ սեղմիր «🎮 Սկսել խաղը»։")

# ✅ Message handler — խաղ, վճարել եմ, սկսել, օգնություն
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text.strip().lower()

    # Սկսել խաղը
    if text == "🎮 սկսել խաղը":
        await start(update, context)
        return
    elif text == "ℹ️ օգնություն":
        await help_command(update, context)
        return

    # Վճարել եմ
    if "վճարել եմ" in text or "վճարված է" in text:
        pending_verifications[user_id] = update.message.from_user.full_name
        await update.message.reply_text("✅ Հարցումը ուղարկվել է ադմինին։")

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("✅ Հաստատել", callback_data=f"approve_{user_id}"),
             InlineKeyboardButton("❌ Չեղարկել", callback_data=f"cancel_{user_id}")]
        ])

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"💸 {pending_verifications[user_id]} գրել է «{update.message.text}»:",
            reply_markup=keyboard
        )
        return

    # Եթե user-ը դեռ չունի խաղ, սկսի
    if user_id not in users_data:
        await start(update, context)
        return

    # Թվային փորձ
    try:
        guess = int(text)
    except ValueError:
        await update.message.reply_text("Մուտքագրիր ամբողջ թիվ։")
        return

    data = users_data[user_id]
    if data["attempts_left"] <= 0:
        await update.message.reply_text("Փորձերդ վերջացել են ❌\nՎճարիր՝ նորից սկսելու համար։")
        return

    data["attempts_left"] -= 1
    if guess == data["target"]:
        await update.message.reply_text("🎉 Ճիշտ գուշակեցիր! Նոր թիվ եմ մտածում...")
        data["target"] = random.randint(1, 100)
        data["attempts_left"] = 5 if not data["paid"] else 20
    elif guess < data["target"]:
        await update.message.reply_text(f"📉 Ավելի բարձր թիվ։ Մնաց {data['attempts_left']} փորձ։")
    else:
        await update.message.reply_text(f"📈 Ավելի ցածր թիվ։ Մնաց {data['attempts_left']} փորձ։")

# ✅ Հաստատում/չեղարկում callback
async def approve_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.from_user.id != ADMIN_ID:
        await query.edit_message_text("❌ Դուք իրավունք չունեք այս գործողությունն անել։")
        return

    data = query.data
    user_id = int(data.split("_")[1])

    if data.startswith("approve_"):
        if user_id in users_data:
            users_data[user_id]["paid"] = True
            users_data[user_id]["attempts_left"] += 20
            await context.bot.send_message(chat_id=user_id,
                text="✅ Վճարումը հաստատվեց։ Ստացար 20 նոր փորձ։")
            await query.edit_message_text("Վճարումը հաստատվեց ✅")
        else:
            await query.edit_message_text("❌ Այդ user-ը խաղը չի սկսել։")
        pending_verifications.pop(user_id, None)

    elif data.startswith("cancel_"):
        await context.bot.send_message(chat_id=user_id,
            text="❌ Ձեր վճարումը մերժվել է ադմինի կողմից։")
        await query.edit_message_text("Վճարումը չեղարկվեց ❌")
        pending_verifications.pop(user_id, None)

# ▶️ Bot setup
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
app.add_handler(CallbackQueryHandler(approve_callback))

print("Բոտը ակտիվ է ✅")
app.run_polling()

