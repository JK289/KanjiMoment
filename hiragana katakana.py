vowel_list = ['a', 'i', 'u', 'e', 'o']
consonant_list = ['k', 's', 't', 'n', 'h', 'm', 'y', 'r', 'w', 'n', 'g', 'z', 'd', 'b', 'p', 'j', 'f']

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
                 'ゃ', 'ゅ', 'ょ', 'っ']

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
                 'ャ', 'ュ', 'ョ', 'ッ']

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
               '*ya', '*yu', '*yo', 'k', 's', 't', 'h', 'm', 'r', 'g', 'z', 'd', 'p', 'b']


# x_y from x writing system to y writing system

def split_romaji(rom_word):
    word = ''
    i = 0
    rom_word = rom_word + '     '
    while rom_word[i] != ' ':
        if rom_word[i] + rom_word[i + 1] in ['sh', 'ch', 'ts', 'dj', 'dz', '*y']:
            word = word + rom_word[i] + rom_word[i + 1] + rom_word[i + 2] + ' '
            i = i + 3

        if (rom_word[i] in consonant_list) and (rom_word[i + 1] in vowel_list):
            word = word + rom_word[i] + rom_word[i + 1] + ' '
            i = i + 2

        if rom_word[i] in vowel_list or (
                rom_word[i] == 'n' and (rom_word[i + 1] == ' ' or rom_word[i + 1] in consonant_list)):
            word = word + rom_word[i] + ' '
            i = i + 1
    word = word.strip()
    return word


def hir_rom(hir_word):
    rom = ''
    i = -1

    for hir in hir_word:
        i = i + 1
        if hir == 'ウ' and hir_word[i - 1] in ['こ', 'そ', 'と', 'の', 'ほ', 'も', 'ろ', 'ご', 'ぞ', 'ど', 'ぼ', 'ぽ']:
            rom = rom + 'o'  # double o instead of ou like "arigatoo"
        else:
            if hir == 'っ':  # double next consonant when small tsu っ "otto"
                next_mora = romaji_list[hiragana_list.index(hir_word[i + 1])]
                rom = rom + next_mora[0]
            else:
                rom = rom + romaji_list[hiragana_list.index(hir)]

    return rom


def rom_hir(rom_word):
    rom_word = split_romaji(rom_word)
    hir = ''
    rom_word = list(rom_word.split(' '))
    for rom in rom_word:
        if romaji_list.index(rom) > 75:
            hir = hir + 'っ'
        else:
            hir = hir + hiragana_list[romaji_list.index(rom)]  # 75 e k
    return hir


def kat_rom(kat_word):
    rom = ''
    i = -1

    for kat in kat_word:
        i = i + 1
        if kat == 'ー':
            rom = rom + romaji_list[katakana_list.index(kat_word[i - 1])][1]
            # choonpu for long vowels in mora
        else:
            if kat == 'ッ':  # double next consonant when small tsu ッ
                next_mora = romaji_list[katakana_list.index(kat_word[i + 1])]
                rom = rom + next_mora[0]
            else:
                rom = rom + romaji_list[katakana_list.index(kat)]

    return rom


def rom_kat(rom_word):
    rom_word = split_romaji(rom_word)
    kat = ''
    rom_word = list(rom_word.split(' '))
    for rom in rom_word:
        if romaji_list.index(rom) > 75:
            kat = kat + 'ッ'
        else:
            kat = kat + katakana_list[romaji_list.index(rom)]  # 75 e k
    return kat


def hir_kat(hir_word):
    return rom_kat((hir_rom(hir_word)))


def kat_hir(kat_word):
    return rom_hir(kat_rom(kat_word))


print(hir_rom('ありがとうございますすすす'))
print(kat_hir('キムヂョングヒョ'))
print(rom_kat('kimudji*yonguhi*yo'))
