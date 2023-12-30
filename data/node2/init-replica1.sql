CREATE DATABASE replica;

CREATE TABLE replica.users_activities (
    id UUID,
    user_id UUID,
    film_id UUID,
    event_name String,
    comment Nullable(String),
    film_sec Nullable(Int64),
    like Nullable(Bool),
    event_time DateTime
) Engine=ReplicatedMergeTree('/clickhouse/tables/shard1/users_activities', 'replica_2') PARTITION BY toYYYYMMDD(event_time) ORDER BY id;
