import pandas as pd
import json
from datetime import date


class Parser:
    columns = ("name",
               "price",
               "sum",
               "quantity",
               "paymentType",
               "productType",
               "nds",
               "ndsSum",
               "date"
               )

    def parse_to_df(self, filename:str) -> pd.DataFrame:
        with open("data/" + filename) as f:
            raw_data = f.read()
            data = json.loads(raw_data)
        data_day = date.fromtimestamp(data['dateTime'])
        items = data['items']
        results = [

        ]
        for item in items:
            results.append((
                item['name'],
                item['price'],
                item['sum'],
                item['quantity'],
                item['paymentType'],
                item['productType'],
                item['nds'],
                item['ndsSum'],
                data_day
            ))
        df = pd.DataFrame(results)
        df.columns = self.columns
        return df
