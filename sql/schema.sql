CREATE TABLE IF NOT EXISTS `BreastCancerDiagnostic`
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `radius_mean` FLOAT NOT NULL,
    `texture_mean` FLOAT NOT NULL,
    `area_mean` FLOAT NOT NULL,
    `area_se` FLOAT NOT NULL,
    `area_worst` FLOAT NOT NULL,
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;