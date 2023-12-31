import sys
import backoff

from time import sleep
from pathlib import Path
from clickhouse_driver.errors import Error as ClickHouseError
from clickhouse_driver import connect

sys.path.append(str(Path(__file__).resolve().parents[1]))

from settings import settings
from logger import logger


BACKOFF_MAX_TIME = 60


if __name__ == '__main__':
	@backoff.on_exception(
		backoff.expo,
		(ClickHouseError, ),
		max_time=BACKOFF_MAX_TIME
	)
	def wait_for_clickhouse():
		try:
			with connect(
				host=settings.clickhouse_host,
				port=settings.clickhouse_port,
				user=settings.clickhouse_user
			) as connection:
				cursor = connection.cursor()
				cursor.execute('SELECT 1')
				result = cursor.fetchone()
				if result and result[0] == 1:
					logger.info('ClickHouse is available')
					sleep(1)
				else:
					raise ClickHouseError
		except ClickHouseError:
			logger.info('ClickHouse is not available')
			raise ClickHouseError

	wait_for_clickhouse()
