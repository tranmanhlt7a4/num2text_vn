"""
    Thông tin chung:
        ...
"""

NUM_IN_TEXT = {"0": "không", "1": "một", "2": "hai", "3": "ba", "4": "bốn",
               "5": "năm", "6": "sáu", "7": "bảy", "8": "tám", "9": "chín"}

UNIT = {1: "", 2: "mươi", 3: "trăm",
        4: "nghìn", 5: "chục nghìn", 6: "trăm nghìn",
        7: "triệu", 8: "chục triệu", 9: "trăm triệu",
        10: "tỷ", 11: "chục tỷ", 12: "trăm tỷ"}

SPECIAL_FORM = {"một mươi": "mười"}


def special_form_init() -> None:
    for level in UNIT:
        if level == 1:
            continue
        else:
            SPECIAL_FORM["không " + UNIT[level]] = ""


def num_to_raw_list(num: int) -> list[str]:
    str_num_reversed = str(num)[::-1]

    raw_list: list[str] = []
    level = 1

    for i in str_num_reversed:
        raw_list.append(NUM_IN_TEXT[i] + " " + UNIT[level])
        level += 1

    return raw_list[::-1]


def raw_list_to_str(raw_list: list[str]) -> str:
    text: str = ""
    for i in raw_list:
        text += i + " "

    return text


def num2text(num: int) -> str:
    pass


if __name__ == "__main__":
    special_form_init()

    print(num_to_raw_list(12223))
