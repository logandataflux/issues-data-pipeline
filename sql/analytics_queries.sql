/*Ticket volume by status*/
SELECT state, COUNT(*) AS total_tickets
FROM github_issues
GROUP BY state
ORDER BY total_tickets DESC;

/*SLA breakdown*/
SELECT sla_status, COUNT(*) AS count
FROM github_issues
GROUP BY sla_status;

/*Average resolution time*/
SELECT AVG(resolution_time_hours) AS avg_resolution_time
FROM github_issues;

/*Daily ticket trend*/
SELECT DATE(created_at) AS day, COUNT(*) AS tickets
FROM github_issues
GROUP BY day
ORDER BY day;

/*SLA breach rate*/
SELECT 
    ROUND(
        COUNT(*) FILTER (WHERE sla_status = 'Breached') * 100.0 
        / COUNT(*), 2
    ) AS breach_percentage
FROM github_issues;
