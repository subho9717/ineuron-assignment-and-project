CREATE TABLE `FitBit data` (
	`Id` DECIMAL(38, 0) NOT NULL, 
	`ActivityDate` DATE NOT NULL, 
	`TotalSteps` DECIMAL(38, 0) NOT NULL, 
	`TotalDistance` DECIMAL(38, 17) NOT NULL, 
	`TrackerDistance` DECIMAL(38, 17) NOT NULL, 
	`LoggedActivitiesDistance` DECIMAL(38, 15) NOT NULL, 
	`VeryActiveDistance` DECIMAL(38, 17) NOT NULL, 
	`ModeratelyActiveDistance` DECIMAL(38, 16) NOT NULL, 
	`LightActiveDistance` DECIMAL(38, 17) NOT NULL, 
	`SedentaryActiveDistance` DECIMAL(38, 17) NOT NULL, 
	`VeryActiveMinutes` DECIMAL(38, 0) NOT NULL, 
	`FairlyActiveMinutes` DECIMAL(38, 0) NOT NULL, 
	`LightlyActiveMinutes` DECIMAL(38, 0) NOT NULL, 
	`SedentaryMinutes` DECIMAL(38, 0) NOT NULL, 
	`Calories` DECIMAL(38, 0) NOT NULL
);
