
uighur_cyrillic = '''
IX-XIII әсирләрдә тарихий вәтинимизниң ғәрбий-шималий егизлиги бир қисмида
Таңғутлар һакимийити, Хиши коридорида Гәнҗу уйғур һакимийити, Турпан
ойманлиғи вә униң әтрапида Қочу (Турпан) уйғур һакимийити, Қучаниң Ғәриптин
Бухарағичә һәм Шималий Иссиқ көлдин тартип җәнупта Хотәнгичә болған зиминда
Қараханийлар һакимийити моҗут еди.
Қараханийлар дөлити дәсләп Баласағун шәһирини, андин Қәшқәр (Орда кәнтини)
пайтәхт қилди. Уйғур хәлқи әҗдатлири тәрипидин қурулған. Ушбу Қараханийлар сулалә
миладийә ІХ әсирдин ХІІІ әсирниң башлириғичә һөкүм сүридекән, болупму Оттура
Асия зимининиң ихтисадий һәм мәдәний тәрәққиятида муһим роль ойниған еди.
Қараханийлар ХІ әсирдә йеза егилик, қолһүнәр санаити вә иҗтимаий ишләпчиқириши
асасида олтирақлишип умумлашқан еди. Шу чағда Қәшқәр, Барчуқ (Маралбеши),

Баласағун, Отрар, Фараб, Мәрғинан, сәмәрқәнд, Бухара қатарлиқ шәһәрләрдә жи-
рик ихтисадий мәдәнийәт мәркәзлири шәкилләнгән. Қараханийлар егилигән кәң

зимин мәмурий җәһәттин үч чоң қисимларға бөлүнгән: биринчидин, Қәшқәр вә
Баласағунни пайтәхт қилған мәркизий қисим, бу зимин «Хақанийә өлкиси» дәп
аталған. Иккинчидин, сәмәрқәнд вә Таласни мәркәз қилған ғәрбий қисим, үчинчидин,
Хотәнни мәркәз қилған шәрқий-җәнубий қисим болуп, кейинки иккинчи қисми «Илик
хақан» дәп аталған Қәшқәр «Орда кәнт» дейилгән. Мәнаси хан туридиған мәркизий
шәһәр демәктур.
'''

substitutesDict = {
    'A': 'A',
    'Ә': 'E',
    'Б': 'B',
    'В': 'W',
    'Г': 'G',
    'Ғ': 'Gh',
    'Д': 'D',
    'Е': 'Ë',
    'Ж': 'Zh',
    'Җ': 'J',
    'З': 'Z',
    'И': 'I',
    'Й': 'Y',
    'К': 'K',
    'Қ': 'Q',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'Ң': 'Ng',
    'О': 'O',
    'Ө': 'Ö',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ү': 'Ü',
    'Ф': 'F',
    'Х': 'X',
    'Һ': 'H',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Ю': 'Yu',
    'Я': 'Ya',
    'a': 'a',
    'ә': 'e',
    'б': 'b',
    'в': 'w',
    'г': 'g',
    'ғ': 'gh',
    'д': 'd',
    'е': 'ë',
    'ж': 'zh',
    'җ': 'j',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'қ': 'q',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'ң': 'ng',
    'о': 'o',
    'ө': 'ö',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ү': 'ü',
    'ф': 'f',
    'х': 'x',
    'һ': 'H',
    'ч': 'ch',
    'ш': 'sh',
    'ю': 'yu',
    'я': 'ya',
}


def linear_substitute(text):
    new_text = ''
    for symbol in text:
        if symbol == 'ь' or symbol == 'ъ':
            continue
        new_text += substitutesDict.get(symbol) if substitutesDict.get(symbol) is not None else symbol
    return new_text


if __name__ == '__main__':
    for key, val in substitutesDict.items():
        if key == '' or val == '':
            print(key, val)
