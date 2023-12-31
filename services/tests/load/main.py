import random
import uuid

from locust import HttpUser, task


class UGCServiceUser(HttpUser):
	@task
	def set_like(self):
		self.client.post(
			'/ugc/api/v1/statistic/post_event',
			json={
				'user_id': str(uuid.uuid4()),
				'film_id': str(uuid.uuid4()),
				'event_name': 'film_likes',
				'like': True
			}
		)
	@task
	def set_comment(self):
		self.client.post(
			'/ugc/api/v1/statistic/post_event',
			json={
				'user_id': str(uuid.uuid4()),
				'film_id': str(uuid.uuid4()),
				'event_name': 'film_comments',
				'comment': 'user comment'
			}
		)
	@task
	def set_film_history(self):
		self.client.post(
			'/ugc/api/v1/statistic/post_event',
			json={
				'user_id': str(uuid.uuid4()),
				'film_id': str(uuid.uuid4()),
				'event_name': 'film_history',
				'film_sec': 10
			}
		)
