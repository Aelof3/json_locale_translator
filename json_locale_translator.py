# python3.10
import json
import copy
import os
import argparse
from python_translator import Translator
from pathlib import Path

# possible languages [language, code]:
lang_opt_list = [["Afrikaans","af"],["Albanian","sq"],["Amharic","am"],["Arabic","ar"],["Armenian","hy"],["Assamese","as"],["Aymara","ay"],["Azerbaijani","az"],["Bambara","bm"],["Basque","eu"],["Belarusian","be"],["Bengali","bn"],["Bhojpuri","bho"],["Bosnian","bs"],["Bulgarian","bg"],["Catalan","ca"],["Cebuano","ceb"],["Chinese (Simplified)","zh"],["Chinese (Traditional)","zh-TW"],["Corsican","co"],["Croatian","hr"],["Czech","cs"],["Danish","da"],["Dhivehi","dv"],["Dogri","doi"],["Dutch","nl"],["English","en"],["Esperanto","eo"],["Estonian","et"],["Ewe","ee"],["Filipino (Tagalog)","fil"],["Finnish","fi"],["French","fr"],["Frisian","fy"],["Galician","gl"],["Georgian","ka"],["German","de"],["Greek","el"],["Guarani","gn"],["Gujarati","gu"],["Haitian Creole","ht"],["Hausa","ha"],["Hawaiian","haw"],["Hebrew","he"],["Hindi","hi"],["Hmong","hmn"],["Hungarian","hu"],["Icelandic","is"],["Igbo","ig"],["Ilocano","ilo"],["Indonesian","id"],["Irish","ga"],["Italian","it"],["Japanese","ja"],["Javanese","jv"],["Kannada","kn"],["Kazakh","kk"],["Khmer","km"],["Kinyarwanda","rw"],["Konkani","gom"],["Korean","ko"],["Krio","kri"],["Kurdish","ku"],["Kurdish (Sorani)","ckb"],["Kyrgyz","ky"],["Lao","lo"],["Latin","la"],["Latvian","lv"],["Lingala","ln"],["Lithuanian","lt"],["Luganda","lg"],["Luxembourgish","lb"],["Macedonian","mk"],["Maithili","mai"],["Malagasy","mg"],["Malay","ms"],["Malayalam","ml"],["Maltese","mt"],["Maori","mi"],["Marathi","mr"],["Meiteilon (Manipuri)","mni-Mtei"],["Mizo","lus"],["Mongolian","mn"],["Myanmar (Burmese)","my"],["Nepali","ne"],["Norwegian","no"],["Nyanja (Chichewa)","ny"],["Odia (Oriya)","or"],["Oromo","om"],["Pashto","ps"],["Persian","fa"],["Polish","pl"],["Portuguese (Portugal, Brazil)","pt"],["Punjabi","pa"],["Quechua","qu"],["Romanian","ro"],["Russian","ru"],["Samoan","sm"],["Sanskrit","sa"],["Scots Gaelic","gd"],["Sepedi","nso"],["Serbian","sr"],["Sesotho","st"],["Shona","sn"],["Sindhi","sd"],["Sinhala (Sinhalese)","si"],["Slovak","sk"],["Slovenian","sl"],["Somali","so"],["Spanish","es"],["Sundanese","su"],["Swahili","sw"],["Swedish","sv"],["Tagalog (Filipino)","tl"],["Tajik","tg"],["Tamil","ta"],["Tatar","tt"],["Telugu","te"],["Thai","th"],["Tigrinya","ti"],["Tsonga","ts"],["Turkish","tr"],["Turkmen","tk"],["Twi (Akan)","ak"],["Ukrainian","uk"],["Urdu","ur"],["Uyghur","ug"],["Uzbek","uz"],["Vietnamese","vi"],["Welsh","cy"],["Xhosa","xh"],["Yiddish","yi"],["Yoruba","yo"],["Zulu","zu"]]

parser = argparse.ArgumentParser(
                    prog='json_locale_translator',
                    description='Translate your locale json files using any language available at https://translate.google.com/',
                    epilog='Example: python3.10 json_locale_translator.py -b en -d locales -l hi ar es fr pt ja')


parser.add_argument('-f', '--file', help='Source file name, located in the destination folder. Default: (base language code).json e.g. en.json')
parser.add_argument('-b', '--base', help='Base language code. Default (english): en')
parser.add_argument('-d', '--dest', help='Destination folder for the translated files. Default: locales')
parser.add_argument('-l', '--langs', nargs='+', help='List of languages to translate to, by language code. Example: -l hi ar es fr pt ja')
parser.add_argument('-F', '--force', action='store_true', help='Force update all translations (even if they already exist). Default: False')
parser.add_argument('-s', '--sort', action='store_true', help='Sort the base language keys alphabetically. Default: False')
parser.add_argument('-L', '--list', action='store_true', help='List all available languages')

args = parser.parse_args()

if args.list:
    print('Available languages:')
    for i in range(len(lang_opt_list)):
        print(lang_opt_list[i][0] + ' - ' + lang_opt_list[i][1])
    exit()


# force update all translations
FORCE_FULL_UPDATE = args.force or False

# sort the base language keys alphabetically
SORT_BASE_LANGUAGE_KEYS = args.sort or False

# can use any language from https://translate.google.com/ (as listed above)
# language: [name, code] - code is used for output file name

default_language_list = [
    ['hindi', 'hi'], 
    ['arabic', 'ar'], 
    ['spanish', 'es'], 
    ['french', 'fr'], 
    ['portuguese', 'pt'], 
    ['japanese', 'ja']
]

# if args.langs exists, create language list from it
if args.langs:
    language_list = []
    for i in range(len(args.langs)):
        for j in range(len(lang_opt_list)):
            if args.langs[i] == lang_opt_list[j][1]:
                language_list.append([lang_opt_list[j][0], lang_opt_list[j][1]])
                break
else:
    language_list = default_language_list



# output relative path
DEST_PATH = Path('./locales')

# source code
source_language_code = args.base or 'en'

# find source language name from code
source_language = ''
for i in range(len(lang_opt_list)):
    if source_language_code == lang_opt_list[i][1]:
        source_language = lang_opt_list[i][0]
        break

if source_language == '':
    print('Invalid source language code: ' + source_language_code)
    exit()

source_file = args.file or source_language_code + '.json'

if SORT_BASE_LANGUAGE_KEYS:
    language_list.append([source_language, source_language_code])

# load source file
jsondata = json.load(open(DEST_PATH / source_file, encoding='utf-8'))
translator = Translator()

def countKeysInObject(obj):
    count = 0
    for key in obj:
        if type(obj[key]) is str:
            count += 1
        else:
            count += countKeysInObject(obj[key])
    return count

langListKeyCount = countKeysInObject(jsondata)
totalKeys = langListKeyCount * len(language_list)

currentCount = 0
langCount = 0

# recursive translate function
def tx(data, langdata, dest):
    for key in data:
        if type(data[key]) is str:
            global currentCount
            global langCount
            
            currentCount += 1
            langCount += 1
            
            print(('Translating - total: %d/%d | %s: %d/%d' + (" " * 50)) % (currentCount,totalKeys,dest,langCount,langListKeyCount), end='\r', flush=True)
            
            if key in langdata and not FORCE_FULL_UPDATE:
                data[key] = langdata[key]
                continue
                
            res = translator.translate(data[key], dest, source_language)
            data[key] = res.new_text
        else:
            l = {}
            if key in langdata and not FORCE_FULL_UPDATE:
                l = langdata[key]
            
            data[key] = tx(data[key], l, dest)

    return data


def main():
    for i in range(len(language_list)):
        langCount = 0
        language = language_list[i][0]
        language_code = language_list[i][1]

        jsonlangdata = {}
        if language_code + '.json' in os.listdir(DEST_PATH):
            jsonlangdata = json.load(open(DEST_PATH / f'{language_code}.json', encoding='utf-8'))
        
        tmpdata = copy.deepcopy(jsondata)
        tmplangdata = copy.deepcopy(jsonlangdata)

        newdata = tx(tmpdata, tmplangdata, language)

        newfile = open(DEST_PATH / f'{language_code}.json', 'w', encoding='utf-8')
        newfile.write(json.dumps(newdata, indent=4, sort_keys=True, ensure_ascii=False))
        newfile.close()

        print((language + ' (DONE)' + (" " * 50) + '\n'), end='\r', flush=True)


if __name__ == "__main__":
    main()