import sqlite3
import requests


class DBDataSetWriter:
    def __init__(self, db_filename, dataset_url):
        self.db_file = db_filename
        self.db_connector = self.create_database()
        self.dataset_url = dataset_url
        self.data = self.get_data_from_url()
        self.dataset_table = ''
        self.db_cursor = self.db_connector.cursor()

    def __del__(self):
        self.db_connector.close()

    def get_data_from_url(self):
        response = requests.get(self.dataset_url)
        data = response.text.split("\n")
        datalist = []
        for row in data:
            datalist_row = []
            for element in row.split(";"):
                datalist_row.append(element.replace('"', ''))
            if len(datalist_row) > 1:
                datalist.append(datalist_row)
        return {
            'columns': datalist[0],
            'data': datalist[1:],
        }

    def create_database(self):
        connection = sqlite3.connect(self.db_file)
        return connection

    def create_table(self, table_name):
        columns = " TEXT, ".join(self.data['columns'])
        columns += " TEXT"
        self.db_cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (Title TEXT, Director TEXT, Year INT)")
        self.dataset_table = table_name

    def write_data(self, part_count):
        dataset = [row for row in self.data['data']]
        separated_dataset = [dataset[i::part_count] for i in range(part_count)]
        for part in separated_dataset:
            self.db_cursor.executemany(f"INSERT INTO {self.dataset_table} VALUES (?, ?, ?)", part)
        self.db_connector.commit()


if __name__ == "__main__":
    dbDataSet = DBDataSetWriter('db.sqlite3', 'https://worldweather.wmo.int/en/json/full_city_list.txt')
    dbDataSet.create_table('dataset')
    dbDataSet.write_data(50)
