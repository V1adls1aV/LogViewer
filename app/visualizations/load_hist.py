import pandas as pd

class HistOfLoad:
    def __init__(self, data: pd.DataFrame, datetime_fmt: str):
        self.data = data
        self.datetime_fmt = datetime_fmt

    def plot(self, segment_count: int) -> list[int] | None:
        datetime_column = self._get_datetime_column(self.data.columns)
        if datetime_column is not None:
            new = pd.to_datetime(
                self.data[datetime_column].map(lambda x: x.split(',')[0]),
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
