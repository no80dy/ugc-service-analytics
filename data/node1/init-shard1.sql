CREATE DATABASE shard;

CREATE TABLE shard.users_activities (
    id Int64,
    user_id UUID,
    film_id UUID,
    event_name String,
    comment String,
    film_sec Int64,
    event_time DateTime
) Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/users_activities', 'replica_1') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;

CREATE TABLE default.users_activities (
    id Int64,
    user_id UUID,
    film_id UUID,
    event_name String,
    comment String,
    film_sec Int64,
    event_time DateTime
) ENGINE = Distributed('company_cluster', '', users_activities, rand());