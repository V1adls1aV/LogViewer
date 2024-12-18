import pandas as pd
import re

class HistOfLoad:
    def __init__(self, data: pd.DataFrame, datetime_fmt: str):
        self.data = data
        self.datetime_fmt = datetime_fmt

    def plot(self, segment_count: int) -> list[int] | None:
        datetime_column = self._get_datetime_column(self.data.columns)
        if datetime_column is not None:
            new = pd.to_datetime(
                self._remove_milliseconds(self.data[datetime_column]),
                format=self.datetime_fmt).tolist()

            start = new[0]
            end = new[-1]
            delta = (end - start) / segment_count

            time = []
            log_count = []

            i = 0
            left = start
            while left < end:
                cnt = 0
                right = left + delta
                while new[i] < right:
                    i += 1
                    cnt += 1
                    if i >= len(new):
                        break

                time.append(str(left))
                log_count.append(cnt)

                left += delta

            return log_count

    def _get_datetime_column(self, columns: list[str]) -> str | None:
        for col in columns:
            if 'time' in col.lower() or 'date' in col.lower():
                return col

    def _remove_milliseconds(self, df: pd.Series) -> pd.Series:
        for i in range(len(df)):
            df[i] = re.sub(r',\d+', '', df[i])
        return df
