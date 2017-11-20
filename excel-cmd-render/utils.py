import os

# copy text to mac pasteboard
def copy_text_to_mac_pasteboard(text):
    encode_text = text.replace('$', '\$')
    cmd = 'echo "{text}" | pbcopy'.format(text=encode_text)
    os.system(cmd)