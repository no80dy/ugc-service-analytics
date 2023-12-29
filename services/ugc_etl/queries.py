insert_query = (
	"INSERT INTO default.users_activities (id, user_id, film_id, event_name, comment, film_sec, event_time)"
	"VALUES (%(id)s, %(user_id)s, %(film_id)s, %(event_name)s, %(comment)s, %(film_sec)s, %(event_time)s)"
)