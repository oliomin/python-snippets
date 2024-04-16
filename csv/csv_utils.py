import csv


def get_csv_col_names(filename):
	with open(filename) as file:
		reader = csv.reader(file)
		for row in reader:
			return row

def csv_yield(filename, /, *cols, first_row_is_headers = True, col_indices = None):
	with open(filename, newline='') as file:
		reader = csv.reader(file)
		for _, row in enumerate(reader):
			if (not _) and first_row_is_headers:
				_headers = [*row]
				continue
			if cols:
				yield [row[_headers.index(_)] for _ in cols]
			elif col_indices:
				yield [row[__] for __ in col_indices]
			else:
				yield row

def csv_yeet(filename, *, mode = 'a', rows):
	with open(filename, newline='', mode = mode) as file:
		writer = csv.writer(file)
		writer.writerows(rows)