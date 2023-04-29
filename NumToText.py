"""
    Chương trình chuyển số sang chữ
    Phạm vi chuyển đổi từ 0 đến 999,999,999,999 (12 chữ số)
"""

# HẰNG SỐ
# Cách đọc của các chữ số
NUM_IN_TEXT: dict[str, str] = {"0": "không", "1": "một", "2": "hai", "3": "ba", "4": "bốn",
                               "5": "năm", "6": "sáu", "7": "bảy", "8": "tám", "9": "chín"}

# Đơn vị (tính từ hàng đơn vị là 1 để đếm lên các hàng trên)
UNIT: dict[int, str] = {1: "", 2: "mươi", 3: "trăm",
                        4: "nghìn", 5: "mươi", 6: "trăm",
                        7: "triệu", 8: "mươi", 9: "trăm",
                        10: "tỷ", 11: "mươi", 12: "trăm"}

# !IMPORTANT: Các trường hợp đặc biệt mà không hiện ra bắt buộc phải để cuối danh sách
# !IMPORTANT: để sau khi xử lí thô xong có thể loại bỏ các phần đặc biệt đó đi.
SPECIAL_CASE: dict[str, str] = {"một mươi": "mười",
                                "mươi một": "mươi mốt",
                                "không mươi": "linh",
                                "mươi không": "mươi",
                                "mười không": "mười",
                                "linh mốt": "linh một",
                                "mươi năm": "mươi lăm",
                                "linh không": ""}


class NumToText():
    '''
        Class dùng để chuyển số về dạng chữ

        Phương thức tĩnh:
            convert(number: int) -> str
        Dùng để lấy dạng chữ của số được truyền vào
    '''

    def __init__(self, number: int = 0) -> None:
        self.__number: int = number

        try:
            self.__out_of_range_check()
        except AssertionError:
            raise ValueError("\n\t(X) Số ngoài phạm vi! (Tối đa 12 chữ số)")

        self.__text: str = ""
        self.__generate_text()
        self.__text = self.__text.strip()

    def __out_of_range_check(self):
        num_str = str(self.__number)
        assert(len(num_str) <= 12)

    def __generate_text(self) -> None:
        number_with_unit = self.__number_with_unit()
        self.__text = ' '.join(number_with_unit)
        self.__process_special_case()

    def __process_special_case(self) -> None:
        for special_case in SPECIAL_CASE:
            if special_case in self.__text:
                self.__text = self.__text.replace(
                    special_case, SPECIAL_CASE[special_case])

        self.__text = self.__text.replace("  ", " ")

    def __is_rounded_number(self):
        num_str = str(self.__number)
        num_str_reversed = num_str[::-1]
        num_reversed = int(num_str_reversed)
        num_reversed_str = str(num_reversed)

        return len(num_reversed_str) == 1

    def __number_with_unit(self) -> list[str]:
        result: list[str] = []

        if self.__is_rounded_number():
            result.append(NUM_IN_TEXT[str(self.__number)[
                          0]] + " " + UNIT[len(str(self.__number))])
        else:
            reversed_number_str = str(self.__number)[::-1]
            level = 1
            for number in reversed_number_str:
                result.append(NUM_IN_TEXT[number] + " " + UNIT[level])
                level += 1

        result = result[::-1]
        return result

    def number(self) -> int:
        return self.__number

    def text(self) -> str:
        return self.__text

    @staticmethod
    def convert(number: int) -> str:
        num_in_text = NumToText(number)
        return num_in_text.text()
