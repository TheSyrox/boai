from boai import *
tr_to_en = Translate(text="Merhaba, nasılsın?", target_lang="en")
print(tr_to_en.translated_text)
