# 🌎 json_locale_translator 🌎
*created by: Richard Folea*

*This tool is for translating locale json files, such as with i18n*
*enjoy* 😃 

---  

### Usage and Options:
```
usage: json_locale_translator [-h] [-f FILE] [-b BASE] [-d DEST] [-l LANGS [LANGS ...]] [-F] [-s] [-L]

Translate your locale json files using any language available at https://translate.google.com/ 

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Source file name, located in the destination folder. Default: (base language code).json e.g. en.json
  -b BASE, --base BASE  Base language code. Default (english): en
  -d DEST, --dest DEST  Destination folder for the translated files. Default: locales
  -l LANGS [LANGS ...], --langs LANGS [LANGS ...]
                        List of languages to translate to, by language code. Example: -l hi ar es fr pt ja
  -F, --force           Force update all translations (even if they already exist). Default: False
  -s, --sort            Sort the base language keys alphabetically. Default: False
  -L, --list            List all available languages (or any from google translate that are missing)
```

---

### Example:
```bash
$ python3.10 json_locale_translator.py -l es 
```

### English locale file (locales/en.json):
```json
{
    "phrases": {
        "hello": "Hello",
        "world": "World"
    },
    "nested": {
        "objects": {
            "ball": "Ball",
            "car": "Car",
            "house": "House"
        },
        "fruits": {
            "apple": "Apple",
            "banana": "Banana",
            "orange": "Orange"
        },
        "vegetables": {
            "carrot": "Carrot",
            "potato": "Potato",
            "tomato": "Tomato"
        },
        "nestedAgain": {
            "plants": {
                "flower": "Flower",
                "tree": "Tree",
                "grass": "Grass",
                "bush": "Bush"
            },
            "animals": {
                "dog": "Dog",
                "cat": "Cat",
                "bird": "Bird",
                "fish": "Fish"
            }
        }
    }
}
```

### Translates to Spanish locale file (locales/es.json):
```json
{
    "nested": {
        "fruits": {
            "apple": "Manzana",
            "banana": "Banana",
            "orange": "Naranja"
        },
        "nestedAgain": {
            "animals": {
                "bird": "Pájaro",
                "cat": "Gato",
                "dog": "Perro",
                "fish": "Pez"
            },
            "plants": {
                "bush": "Arbusto",
                "flower": "Flor",
                "grass": "Césped",
                "tree": "Árbol"
            }
        },
        "objects": {
            "ball": "Pelota",
            "car": "Auto",
            "house": "Casa"
        },
        "vegetables": {
            "carrot": "Zanahoria",
            "potato": "Papa",
            "tomato": "Tomate"
        }
    },
    "phrases": {
        "hello": "Hola",
        "world": "Mundo"
    }
}
```

---

### Language list from google translate (as of July 27th, 2023)
```
CODE            LANGUAGE
-------------------------
af ............ Afrikaans
sq ............ Albanian
am ............ Amharic
ar ............ Arabic
hy ............ Armenian
as ............ Assamese
ay ............ Aymara
az ............ Azerbaijani
bm ............ Bambara
eu ............ Basque
be ............ Belarusian
bn ............ Bengali
bho ........... Bhojpuri
bs ............ Bosnian
bg ............ Bulgarian
ca ............ Catalan
ceb ........... Cebuano
zh ............ Chinese (Simplified)
zh-TW ......... Chinese (Traditional)
co ............ Corsican
hr ............ Croatian
cs ............ Czech
da ............ Danish
dv ............ Dhivehi
doi ........... Dogri
nl ............ Dutch
en ............ English
eo ............ Esperanto
et ............ Estonian
ee ............ Ewe
fil ........... Filipino (Tagalog)
fi ............ Finnish
fr ............ French
fy ............ Frisian
gl ............ Galician
ka ............ Georgian
de ............ German
el ............ Greek
gn ............ Guarani
gu ............ Gujarati
ht ............ Haitian Creole
ha ............ Hausa
haw ........... Hawaiian
he ............ Hebrew
hi ............ Hindi
hmn ........... Hmong
hu ............ Hungarian
is ............ Icelandic
ig ............ Igbo
ilo ........... Ilocano
id ............ Indonesian
ga ............ Irish
it ............ Italian
ja ............ Japanese
jv ............ Javanese
kn ............ Kannada
kk ............ Kazakh
km ............ Khmer
rw ............ Kinyarwanda
gom ........... Konkani
ko ............ Korean
kri ........... Krio
ku ............ Kurdish
ckb ........... Kurdish (Sorani)
ky ............ Kyrgyz
lo ............ Lao
la ............ Latin
lv ............ Latvian
ln ............ Lingala
lt ............ Lithuanian
lg ............ Luganda
lb ............ Luxembourgish
mk ............ Macedonian
mai ........... Maithili
mg ............ Malagasy
ms ............ Malay
ml ............ Malayalam
mt ............ Maltese
mi ............ Maori
mr ............ Marathi
mni-Mtei ...... Meiteilon (Manipuri)
lus ........... Mizo
mn ............ Mongolian
my ............ Myanmar (Burmese)
ne ............ Nepali
no ............ Norwegian
ny ............ Nyanja (Chichewa)
or ............ Odia (Oriya)
om ............ Oromo
ps ............ Pashto
fa ............ Persian
pl ............ Polish
pt ............ Portuguese (Portugal, Brazil)
pa ............ Punjabi
qu ............ Quechua
ro ............ Romanian
ru ............ Russian
sm ............ Samoan
sa ............ Sanskrit
gd ............ Scots Gaelic
nso ........... Sepedi
sr ............ Serbian
st ............ Sesotho
sn ............ Shona
sd ............ Sindhi
si ............ Sinhala (Sinhalese)
sk ............ Slovak
sl ............ Slovenian
so ............ Somali
es ............ Spanish
su ............ Sundanese
sw ............ Swahili
sv ............ Swedish
tl ............ Tagalog (Filipino)
tg ............ Tajik
ta ............ Tamil
tt ............ Tatar
te ............ Telugu
th ............ Thai
ti ............ Tigrinya
ts ............ Tsonga
tr ............ Turkish
tk ............ Turkmen
ak ............ Twi (Akan)
uk ............ Ukrainian
ur ............ Urdu
ug ............ Uyghur
uz ............ Uzbek
vi ............ Vietnamese
cy ............ Welsh
xh ............ Xhosa
yi ............ Yiddish
yo ............ Yoruba
zu ............ Zulu
```