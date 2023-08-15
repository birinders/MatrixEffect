import colorama as cl

cl_black = cl.Fore.BLACK
cl_blue = cl.Fore.BLUE
cl_cyan = cl.Fore.CYAN
cl_green = cl.Fore.GREEN
cl_lightblack = cl.Fore.LIGHTBLACK_EX
cl_lightblue = cl.Fore.LIGHTBLUE_EX
cl_lighcyan = cl.Fore.LIGHTCYAN_EX
cl_lightgreen = cl.Fore.LIGHTGREEN_EX
cl_lightmagenta = cl.Fore.LIGHTMAGENTA_EX
cl_lightred = cl.Fore.LIGHTRED_EX
cl_lightwhite = cl.Fore.LIGHTWHITE_EX
cl_lightyellow = cl.Fore.LIGHTYELLOW_EX
cl_magenta = cl.Fore.MAGENTA
cl_red = cl.Fore.RED
cl_reset = cl.Fore.RESET
cl_white = cl.Fore.WHITE
cl_yellow = cl.Fore.YELLOW

##### Avoid these character sets #####
hebrew = "אבגדהוזחטיכלמננסעפצקרשת"
korean = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅚㅛㅜㅠㅡㅢㅣ"
asian = "ぁぃぅぇぉっゃゅょひふへほまみむめもやゆよらりるれろわんにゃんみゃん"
##### Avoid these character sets #####


greek = "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
cyrillic = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
unique_english = "ůŭŧńşźżñçéáíóúàèìòùœžšžćčđłńó÷øðþæıȷȷłńó÷øðþæ"
kb_symbols = "~!@#$%^&*()_+-={}[]|\\;:<>?/"
english_letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"

letters = greek + cyrillic + unique_english + kb_symbols + english_letters + numbers
n_letters = len(letters)
