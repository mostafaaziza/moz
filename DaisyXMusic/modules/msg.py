# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from DaisyXMusic.config import ASSISTANT_NAME, PROJECT_NAME


class Messages:
    START_MSG = "**هلا 👋 [{}](tg://user?id={})!**\n\nيمكنني تشغيل الموسيقى في الدردشة الصوتية لمجموعتك بالإضافة إلى الدردشات الصوتية للقناة 😸\n\nانقر فوق التالي للحصول على التعليمات."
    HELP_MSG = [
        ".",
        f"""
⋆ مرحبًا بك مرة أخرى {PROJECT_NAME}

يمكنني تشغيل الموسيقى في الدردشة الصوتية لمجموعتك بالإضافة إلى الدردشات الصوتية للقناة ..🙉♥️

⋆ الحساب المساعد >> @{ASSISTANT_NAME}\n\nانقر فوق التالي للحصول على التعليمات
""",
        f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
""",
        f"""
أوامر

= >> تشغيل الأغنية 🎧

- / تشغيل: تشغيل الأغنية المطلوبة
- / play [yt url]: تشغيل عنوان url المحدد في yt
- / تشغيل [رد صوتي]: تشغيل الصوت الذي تم الرد عليه
- / splay: تشغيل الأغنية عبر jio saavn
- / ytplay: تشغيل الأغنية مباشرة عبر Youtube Music

= >> تشغيل ⏯

- / player: افتح قائمة الإعدادات الخاصة بالمشغل
- / تخطي: يتخطى المسار الحالي
- / وقفة: وقفة المسار
- / استئناف: يستأنف المسار المتوقف مؤقتًا
- / end: يوقف تشغيل الوسائط
- / كتم الصوت: كتم تشغيل الأغنية
- / unmute: إلغاء كتم تشغيل الأغنية
- / current: يعرض مسار التشغيل الحالي
- / قائمة التشغيل: تعرض قائمة التشغيل

* مشغل cmd وجميع أوامر cmds الأخرى باستثناء / play و / current و / playlist هي فقط لمشرفي المجموعة.
""",
        f"""
= >> قناة تشغيل الموسيقى 🛠

⚪️ لمسؤولي المجموعة المرتبطة فقط:

- / cplay [اسم الأغنية] - تشغيل الأغنية التي طلبتها
- / csplay [اسم الأغنية] - تشغيل الأغنية التي طلبتها عبر jio saavn
- / cplaylist - عرض قائمة التشغيل الآن
- / cccurrent - عرض قيد التشغيل الآن
- / cplayer - افتح لوحة إعدادات مشغل الموسيقى
- / cpause - إيقاف تشغيل الأغنية مؤقتًا
- / cresume - استئناف تشغيل الأغنية
- / cskip - تشغيل الأغنية التالية
- / cend - إيقاف تشغيل الموسيقى
- / cmute - تشغيل الأغنية الصامتة
- / كتم الصوت - تشغيل الأغنية كتم الصوت
- / إلغاء كتم الصوت - تشغيل الأغنية كتم الصوت
- / userbotjoinchannel - قم بدعوة المساعد إلى الدردشة

يمكن أيضًا استخدام القناة بدلاً من c (/ cplay = / channelplay)

⚪️ إذا كنت لا تحب اللعب في مجموعة مرتبطة:

1) احصل على معرف قناتك.
2) إنشاء مجموعة مع tittle: قناة الموسيقى: your_channel_id
3) أضف البوت كمسؤول قناة مع صلاحيات كاملة
4) أضفMusic_kingoo_hot_bot إلى القناة كمسؤول.
5) ببساطة أرسل الأوامر في مجموعتك. (تذكر استخدام / ytplay بدلاً من ذلك / play)
""",
        f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
        f"""
>> تحميل الأغنية 🎸

- / video [song mame]: تنزيل أغنية الفيديو من youtube
- / song [اسم الأغنية]: تنزيل أغنية صوتية من youtube
- / saavn [اسم الأغنية]: تنزيل أغنية من saavn
- / deezer [اسم الأغنية]: تنزيل الأغنية من deezer

= >> أدوات البحث 📄

- / البحث عن [اسم الأغنية]: ابحث في youtube عن الأغاني
- / lyrics [اسم الأغنية]: احصل على كلمات الأغنية
""",
        f"""
= >> أوامر لمستخدمي سودو ⚔️

 - / userbotleaveall - إزالة المساعد من كافة الدردشات
 - / بث - رد بث عالمي على رسالة لجميع الدردشات
 - / pmpermit [on / off] - تمكين / تعطيل رسالة pmpermit
* يمكن لمستخدمي سودو تنفيذ أي أمر في أي مجموعة

""",
    ]
