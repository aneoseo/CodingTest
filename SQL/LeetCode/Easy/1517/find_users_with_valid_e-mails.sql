SELECT *
FROM Users
WHERE REGEXP_LIKE(mail, '^[[:alpha:]]+[[:alpha:][:digit:]_\\.-]*@leetcode\\.com$', 'c')