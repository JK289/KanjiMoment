vowel_list = ['a', 'i', 'u', 'e', 'o']

consonant_list = ['k', 's', 't', 'n', 'h',
                  'm', 'y', 'r', 'w', 'n',
                  'g', 'z', 'd', 'b', 'p',
                  'j', 'f', 'c']

hiragana_list = ['あ', 'い', 'う', 'え', 'お',
                 'か', 'き', 'く', 'け', 'こ',
                 'さ', 'し', 'す', 'せ', 'そ',
                 'た', 'ち', 'つ', 'て', 'と',
                 'な', 'に', 'ぬ', 'ね', 'の',
                 'は', 'ひ', 'ふ', 'へ', 'ほ',
                 'ま', 'み', 'む', 'め', 'も',
                 'や', 'ゆ', 'よ',
                 'ら', 'り', 'る', 'れ', 'ろ',
                 'わ', 'ゐ', 'ゑ', 'を',
                 'ん',
                 'が', 'ぎ', 'ぐ', 'げ', 'ご',
                 'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
                 'だ', 'ぢ', 'づ', 'で', 'ど',
                 'ば', 'び', 'ぶ', 'べ', 'ぼ',
                 'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',
                 'ゃ', 'ゅ', 'ょ',
                 'きゃ', 'きゅ', 'きょ',
                 'しゃ', 'しゅ', 'しょ',
                 'ちゃ', 'ちゅ', 'ちょ',
                 'にゃ', 'にゅ', 'にょ',
                 'ひゃ', 'ひゅ', 'ひょ',
                 'みゃ', 'みゅ', 'みょ',
                 'りゃ', 'りゅ', 'りょ',
                 'ぎゃ', 'ぎゅ', 'ぎょ',
                 'じゃ', 'じゅ', 'じょ',
                 'ぢゃ', 'ぢゅ', 'ぢょ',
                 'びゃ', 'びゅ', 'びょ',
                 'ぴゃ', 'ぴゅ', 'ぴょ',
                 'っ']

katakana_list = ['ア', 'イ', 'ウ', 'エ', 'オ',
                 'カ', 'キ', 'ク', 'ケ', 'コ',
                 'サ', 'シ', 'ス', 'セ', 'ソ',
                 'タ', 'チ', 'ツ', 'テ', 'ト',
                 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
                 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
                 'マ', 'ミ', 'ム', 'メ', 'モ',
                 'ヤ', 'ユ', 'ヨ',
                 'ラ', 'リ', 'ル', 'レ', 'ロ',
                 'ワ', 'ヰ', 'ヱ', 'ヲ',
                 'ン',
                 'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
                 'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
                 'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
                 'バ', 'ビ', 'ブ', 'ベ', 'ボ',
                 'パ', 'ピ', 'プ', 'ペ', 'ポ',
                 'ャ', 'ュ', 'ョ',
                 'キャ', 'キュ', 'キョ',
                 'シャ', 'シュ', 'ショ',
                 'チャ', 'チュ', 'チョ',
                 'ニャ', 'ニュ', 'ニョ',
                 'ヒャ', 'ヒュ', 'ヒョ',
                 'ミャ', 'ミュ', 'ミョ',
                 'リャ', 'リュ', 'リョ',
                 'ギャ', 'ギュ', 'ギョ',
                 'ジャ', 'ジュ', 'ジョ',
                 'ヂャ', 'ヂュ', 'ヂョ',
                 'ビャ', 'ビュ', 'ビョ',
                 'ピャ', 'ピュ', 'ピョ',
                 'ッ']

romaji_list = ['a', 'i', 'u', 'e', 'o',
               'ka', 'ki', 'ku', 'ke', 'ko',
               'sa', 'shi', 'su', 'se', 'so',
               'ta', 'chi', 'tsu', 'te', 'to',
               'na', 'ni', 'nu', 'ne', 'no',
               'ha', 'hi', 'fu', 'he', 'ho',
               'ma', 'mi', 'mu', 'me', 'mo',
               'ya', 'yu', 'yo',
               'ra', 'ri', 'ru', 're', 'ro',
               'wa', 'wi', 'we', 'wo',
               'n',
               'ga', 'gi', 'gu', 'ge', 'go',
               'za', 'ji', 'zu', 'ze', 'zo',
               'da', 'dji', 'dzu', 'de', 'do',
               'ba', 'bi', 'bu', 'be', 'bo',
               'pa', 'pi', 'pu', 'pe', 'po',
               '*ya', '*yu', '*yo',
               'kya', 'kyu', 'kyo',
               'sha', 'shu', 'sho',
               'cha', 'chu', 'cho',
               'nya', 'nyu', 'nyo',
               'hya', 'hyu', 'hyo',
               'mya', 'myu', 'myo',
               'rya', 'ryu', 'ryo',
               'gya', 'gyu', 'gyo',
               'ja', 'ju', 'jo',
               'dja', 'dju', 'djo',
               'bya', 'byu', 'byo',
               'pya', 'pyu', 'pyo',
               'k', 's', 't', 'h', 'm', 'r', 'g', 'z', 'd', 'p', 'b', 'j']


# x_y from x writing system to y writing system

def split_romaji(rom_word):
    rom_word = rom_word.lower()
    word = ''
    i = 0
    rom_word = rom_word + '   '
    
    while rom_word[i] != ' ':
        if rom_word[i] + rom_word[i + 1] + rom_word[i + 2] in romaji_list:
            word = word + rom_word[i] + rom_word[i + 1] + rom_word[i + 2] + ' '
            i = i + 3
        elif rom_word[i] + rom_word[i + 1] in romaji_list:
            word = word + rom_word[i] + rom_word[i + 1] + ' '
            i = i + 2
        elif rom_word[i] in romaji_list:
            word = word + rom_word[i] + ' '
            i = i + 1
    word = word.strip()
    
    return word


def hr(hir_word):
    rom = ''
    i = 0
    hir_word = hir_word + ' '
    
    while hir_word[i] != ' ':
        if hir_word[i] + hir_word[i + 1] in hiragana_list:  # yoon (digraphs: ぎょ) detection 
            yoon = hir_word[i] + hir_word[i + 1]
            rom = rom + romaji_list[hiragana_list.index(yoon)]
            i = i + 2
        elif hir_word[i] == 'っ':
            mora = romaji_list[hiragana_list.index(hir_word[i + 1])]
            rom = rom + mora[0]
            i = i + 1
        elif hir_word[i + 1] == 'ー':
            mora = romaji_list[hiragana_list.index(hir_word[i])]
            rom = rom + romaji_list[hiragana_list.index(hir_word[i])] + mora[-1]
            i = i + 2
        else:
            rom = rom + romaji_list[hiragana_list.index(hir_word[i])]
            i = i + 1

    return rom


def kr(kat_word):
    rom = ''
    i = 0
    kat_word = kat_word + ' '

    while kat_word[i] != ' ':
        if kat_word[i] + kat_word[i + 1] in katakana_list:  # yoon (digraphs: ニュ) detection 
            yoon = kat_word[i] + kat_word[i + 1]
            rom = rom + romaji_list[katakana_list.index(yoon)]
            i = i + 2
        elif kat_word[i] == 'ッ':
            mora = romaji_list[katakana_list.index(kat_word[i + 1])]
            rom = rom + mora[0]
            i = i + 1
        elif kat_word[i + 1] == 'ー':
            mora = romaji_list[katakana_list.index(kat_word[i])]
            rom = rom + romaji_list[katakana_list.index(kat_word[i])] + mora[-1]
            i = i + 2
        else:
            rom = rom + romaji_list[katakana_list.index(kat_word[i])]
            i = i + 1

    return rom


def rh(rom_word):
    rom_word = split_romaji(rom_word)
    hir = ''
    i = 0
    rom_word = list(rom_word.split(' '))
    rom_word.append(' ')

    while rom_word[i] != ' ':
        if rom_word[i] == 'n':
            hir = hir + 'ん'
            i = i + 1
        elif rom_word[i] == rom_word[i + 1][0]:
            hir = hir + 'っ'
            i = i + 1
        elif rom_word[i] in hiragana_list:
            hir = hir + hiragana_list[romaji_list.index(rom_word[i])]
            i = i + 1
        else:
            hir = hir + hiragana_list[romaji_list.index(rom_word[i])]
            i = i + 1

    return hir


def rk(rom_word):
    rom_word = split_romaji(rom_word)
    kat = ''
    i = 0
    rom_word = list(rom_word.split(' '))
    rom_word.append(' ')

    while rom_word[i] != ' ':

        if rom_word[i] == 'n':
            kat = kat + 'ン'
            i = i + 1
        elif rom_word[i] == rom_word[i + 1][0]:
            kat = kat + 'ッ'
            i = i + 1
        elif rom_word[i] in katakana_list:
            kat = kat + katakana_list[romaji_list.index(rom_word[i])]
            i = i + 1
        else:
            kat = kat + katakana_list[romaji_list.index(rom_word[i])]
            i = i + 1

    return kat


def hk(hir_word):
    return rk(hr(hir_word))


def kh(kat_word):
    return rh(kr(kat_word))


def tte(stce, from_script, to_script):
    from_script = from_script.lower()
    to_script = to_script.lower()
    stce = stce.split()
    tstce = ''

    if from_script == 'romaji' and to_script == 'hiragana':
        for word in stce:
            tstce = tstce + rh(word) + ' '
    elif from_script == 'romaji' and to_script == 'katakana':
        for word in stce:
            tstce = tstce + rk(word) + ' '
    elif from_script == 'hiragana' and to_script == 'romaji':
        for word in stce:
            tstce = tstce + hr(word) + ' '
    elif from_script == 'katakana' and to_script == 'romaji':
        for word in stce:
            tstce = tstce + kr(word) + ' '
    elif from_script == 'hiragana' and to_script == 'katakana':
        for word in stce:
            tstce = tstce + hk(word) + ' '
    elif from_script == 'katakana' and to_script == 'hiragana':
        for word in stce:
            tstce = tstce + kh(word) + ' '

    return tstce
