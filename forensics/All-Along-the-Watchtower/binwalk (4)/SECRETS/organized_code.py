# -*- coding: utf-65536 -*-
def decode(message, shift_value):
    decoded_message = ""
    for char in message:
        num = ord(char) - shift_value
        while num < 0:
            num += 65536
        decoded_char = chr(num)
        decoded_message += decoded_char
    return decoded_message

encoded_message = "啉鹷ꍬ鴠𔑡啥𒁴鰠𓉥𓈠驨啭ꍡ捬褠驨𒄠ꍯ顩慥𓈠驨𒄠ꍯ𓉩顩险𓅮唬鵴啥魯鹦鹣ꍡ啳𒁴捯褠驨啹鹷ꍬ𒄠𖥡售絔𖥥𔔠腩啬ꍡ啬陰捹簠饯ꔠ啹驨饡鴠𓁵𓅴售鵔𓅩鸠啳𓉩鸠𐙳𓈧鸠捴縠ꔧ鰠鹯鱮𓈠啯陲𒅭鱡啥鵴𒁲鱵啨鵴啥𓉳驲𓉥啳驮𓉸𔔠驥捫褠鹨啳𒁲𓍧啥繁鴠𓅡ꔠ饡啥驭鰠𐙯啥陭捤砠靹𓁥𓅰项𒁨鹳啳𓅩𐘠啯除𐙭ꄠꉯ捥縠啴鹷ꍬ霠啥𓁣𠁡捹縠ꔧ頠陲𖥺售𓁃𠁡瑹縠𔔠𓅡頠陲𖥺𒀠顮捥褠驨啹𒁬ꉣ饥ꔠ啥𐙩阠𓀠𒁯慭阠𓀠靵驢啲𒁲ꕯ售啁𓍲面𓁥𓀠𒁯啭鹷鵴𓀠𓉡捳蜠𓉡啳陭驫ꔠ啥𓁣𠁡捹𓁃𠁡瑹砠陲𖥺唿啉陷啳𓁣𠁡啹𐙯驣䄮褊驨啹𓍰啴驭鸠啮啡𒁲ꕯ䄮瘊𓀠靵驢啲𒁲ꕯ䄮瘊𓀠靵驢啲𒁲ꕯ𔔠𓉩啨陲𓅴䄮褊驨啹𓍰啴驭鸠啮啡𓍲面𓁥𓀠𒁯啭鹷鵴𓀠靵驢啲陲𓅴䄮蜊靵驢啲陲𓅴唿啉陨驴𓀠靵驢啲陲𓅴䄮褊驨啹陭驫ꔠ啥𓁣𠁡捹㸍𓁃𠁡瑹縠𔔠𓅡頠陲𖥺𒀠顮捥㸍鵔𖥥𒄠𓉵ꔠ啥𐙩阠𓀠𒁯𦡭𢲀䄮砊陲𖥺唿啉陷啳𓁣𠁡啹𐙯驣䄮褊驨啹𓍰啴驭鸠啮啡𒁲ꕯ䄮瘊𓀠靵驢啲𒁲ꕯ䄮瘊𓀠靵驢啲𒁲ꕯ𔔠𓉩啨陲𓅴䄮褊驨啹𓍰啴驭鸠啮啡𓍲面𓁥𓀠𒁯啭鹷鵴𓀠靵驢啲陲𓅴䄮蜊靵驢啲陲𓅴唿啉陨驴𓀠靵驢啲陲𓅴䄮褊驨啹陭驫ꔠ啥𓁣𠁡捹㸍𓁃𠁡瑹縠𔔠𓅡頠陲𖥺𒀠顮捥㸍鵔𖥥𒄠𓉵ꔠ啥𐙩阠𓀠𒁯𦡭𢲀售㸍㸍㸍顪魴晻椭扭攵樭𓀰𖥲鬭𓀰氭晨𠌵"
shift_value = 617
decoded_message = decode(encoded_message, shift_value)
print(decoded_message)
