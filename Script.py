class script(object):
    START_TXT = """๐ท๐ด๐ปส๐พ {},
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/{}>{}</a>, ๐ธ ๐ฐ๐ผ ๐ฐ ๐ฒ๐พ๐ผ๐ฟ๐ป๐ด๐๐ด ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐+๐ผ๐ฐ๐ฝ๐๐ฐ๐ป ๐ต๐ธ๐ป๐๐ด๐+ ๐ต๐ธ๐ป๐ด ๐๐๐พ๐๐ด ๐ฑ๐พ๐.๐ธ ๐ฒ๐ฐ๐ฝ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด ๐ผ๐พ๐๐ธ๐ด๐, ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ด๐ฝ๐น๐พ๐. ๐"""
    HELP_TXT = """๐ท๐ด๐ {}
สแดส สแดสแด ษชs แดสแด สแดสแด แดา แดส แดแดแดแดแดษดแดs"""
    ABOUT_TXT = """โฏ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: {}
โค๏ธ แดสแดแดแดแดส: <a href=https://t.me/NCM_LINKS>ษดแดแด สษชษดแดs</a>
๐งก สษชสสแดสส: <a href=https://docs.pyrogram.org/>แดสสแดษขสแดแด แดsสษดแดษชแด ๐ท.๐ท๐น.๐ถ</a>
๐ สแดษดษขแดแดษขแด: <a href=https://python.org/>แดสแดสแดษด ๐น.๐ฟ.๐ธ</a>
๐ แดแดแดแด สแดsแด: <a href=https://mongodb.com/>แดแดษดษขแดแดส</a>
๐ค แดส แดสษชแด แดส: <a href=https://motor.readthedocs.io/>แดแดแดแดส แดsสษดแดษชแด ๐ธ.๐ป.๐ท</a>
๐ค ษชแดแดส sแดสแดแดแดแดส: <a href=https://pypi.org/project/IMdBPY>ษชแดแดสแดส</a>
๐ สแดแด sแดสแด แดส : <a href=https://contabo.com/>แดแดษดแดแดสแด</a>
๐ แดษชษดแดแดแด ษขสแดแดแด: <a href=https://t.me/new_cinema_mall>ษดแดแดก แดษชษดแดแดแด แดแดสส</a>"""
    SOURCE_TXT = """<b>NOTE:</b>
- แดแดส แดษชษดแดแดแด ษขสแดแดแด :- @NEW_CINEMA_MALL  

<b>DEVS:</b>
- <a href=https://t.me/NCM_LINKS>ษดแดแด สษชษดแดs</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. <a href=https://t.me/{}>{}</a> should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- <a href=https://t.me/{}>{}</a> Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. <a href=https://t.me/{}>{}</a> supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/new_cinema_mall_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of <a href=https://t.me/{}>{}</a>

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
