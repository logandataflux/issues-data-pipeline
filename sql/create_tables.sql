CREATE TABLE github_issues (
    id BIGINT PRIMARY KEY,
    title TEXT,
    state TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    resolution_time_hours FLOAT,
    sla_status TEXT
);
