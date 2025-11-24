import pyfiglet as pyfiglet
# Render text with the default font
ascii_art = pyfiglet.figlet_format("KJK")
print(ascii_art)
# Render text with a specific font
ascii_art = pyfiglet.figlet_format("KJK", font="slant")
print(ascii_art)
ascii_art = pyfiglet.figlet_format("KJK", font="block")
print(ascii_art)
ascii_art = pyfiglet.figlet_format("KJK", font="bubble")
print(ascii_art)
ascii_art = pyfiglet.figlet_format("KJK", font="digital")
print(ascii_art)