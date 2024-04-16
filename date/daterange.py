from datetime import datetime, timedelta

def daterange(start_date: datetime, end_date: datetime, *, end_inclusive: bool = False) -> Generator[datetime, None, None]:
	'''
		A Genrator Iterator to iterate through days in the given month
	'''
	while start_date < end_date:
		yield start_date
		start_date += timedelta(days = 1)
	if end_inclusive:
		yield start_date
