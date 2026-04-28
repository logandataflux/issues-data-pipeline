/*Check for missing values*/
SELECT *
FROM github_issues
WHERE title IS NULL;

/*Check data distribution*/
SELECT state, COUNT(*)
FROM github_issues
GROUP BY state;
