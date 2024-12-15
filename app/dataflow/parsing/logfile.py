import re
import pandas as pd

from .parser import Parser

class LogFileParser(Parser):
    def parse(self, format: str) -> pd.DataFrame:
        '''
        :param format: Получаем данные в виде StringIO
        :return: Создаем pandas таблицу с именами столбцов и с данными в строках,
        которые передал пользователь
        '''

        log_list = self.data.getvalue().splitlines()
        array_columns = re.findall(r'\{([^{}]*)\}', format)
        pattern = re.sub(r'\{[^{}]*\}', '(.*)', format)

        rows = []
        for log_item in log_list:
            if re.match(pattern, log_item):
                rows.append(
                    re.findall(pattern, log_item)[0]
                )

        return pd.DataFrame(columns=array_columns, data=rows)
