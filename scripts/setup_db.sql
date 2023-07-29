CREATE TABLE indeed_jobs
(
  query_keyword        VARCHAR(50),
  query_location       VARCHAR(50),
  serp                 INT,
  serp_position        INT,
  company              TEXT,
  company_rating       FLOAT,
  company_review_count FLOAT,
  jobkey               VARCHAR(50),
  job_title            VARCHAR(50),
  job_location_city    VARCHAR(50),
  job_location_postal  VARCHAR(50),
  job_location_state   VARCHAR(50),
  max_salary           FLOAT,
  min_salary           FLOAT,
  salary_type          VARCHAR(50),
  pub_date             INT,
  apply_link           VARCHAR(50),
  description          TEXT,
  source               VARCHAR(50)
);

COPY indeed_jobs FROM 'services/crawler/data/indeed_2023-07-28T05-48-56.csv' DELIMITER ',' CSV HEADER;
