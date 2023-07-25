# json_locale_translator  
*created by: Richard Folea*

```js
/** 
 * This tool is for translating locale json files, such as with i18n
 * 
 * enjoy :) 
*/
```

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