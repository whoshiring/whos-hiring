-- CreateTable
CREATE TABLE `IndeedJobs` (
    `job_key` VARCHAR(191) NOT NULL,
    `query_keyword` VARCHAR(191) NOT NULL,
    `query_location` VARCHAR(191) NOT NULL,
    `serp` INTEGER NOT NULL,
    `serp_position` INTEGER NOT NULL,
    `company` VARCHAR(191) NOT NULL,
    `company_rating` DOUBLE NOT NULL,
    `company_review_count` INTEGER NOT NULL,
    `job_title` VARCHAR(191) NOT NULL,
    `description` VARCHAR(191) NOT NULL,
    `apply_link` VARCHAR(191) NOT NULL,
    `posted_at` INTEGER NOT NULL,
    `job_location_city` VARCHAR(191) NOT NULL,
    `job_location_postal` VARCHAR(191) NOT NULL,
    `job_location_state` VARCHAR(191) NOT NULL,
    `max_salary` DOUBLE NOT NULL,
    `min_salary` DOUBLE NOT NULL,
    `salary_type` VARCHAR(191) NOT NULL,
    `source` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`job_key`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
