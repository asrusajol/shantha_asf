# -- invesment_db.investment_snapshots definition

"""CREATE TABLE `investment_snapshots` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_name` varchar(255) DEFAULT NULL,
  `account_type` varchar(50) DEFAULT NULL,
  `investment_type` varchar(50) DEFAULT NULL,
  `units_held` int(11) DEFAULT NULL,
  `investment_cost` decimal(12,2) DEFAULT NULL,
  `market_value` decimal(12,2) DEFAULT NULL,
  `dividend_income` decimal(12,2) DEFAULT NULL,
  `dividend_receivable` decimal(12,2) DEFAULT NULL,
  `total_return` decimal(12,2) DEFAULT NULL,
  `details_url` varchar(255) DEFAULT NULL,
  `snapshot_date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_fund_snapshots_date` (`fund_name`,`snapshot_date`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=ascii COLLATE=ascii_general_ci;"""


# -- invesment_db.nav_history definition

"""CREATE TABLE `nav_history` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fund_name` varchar(255) DEFAULT NULL,
  `nav_date` date DEFAULT NULL,
  `nav_market` decimal(10,4) DEFAULT NULL,
  `buy_price` decimal(10,4) DEFAULT NULL,
  `redemption_price` decimal(10,4) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_fund_nav_date` (`fund_name`,`nav_date`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=ascii COLLATE=ascii_general_ci;"""