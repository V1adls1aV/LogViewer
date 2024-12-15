import pandas as pd

class DataFilter:
    def filter(self, data: pd.DataFrame, column: str, key: str) -> pd.DataFrame:
        '''
        Получаем DataFrame, столбец и значение, по которому фильтровать
        Возвращает новую таблицу с вхождением в столбце
        '''

        return data[data[column].str.contains(key)]
