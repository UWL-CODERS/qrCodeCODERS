import pyqrcode
import png

url = pyqrcode.create('https://discord.gg/CyqRhp6RYm')
url.png('discordQRCode.png', scale = 10, module_color=(31,95,243), background=(255,255,255))
