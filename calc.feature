Feature: testing our calculator

	Scenario: parsing a single digit number
		Given we have imported calc
		 when we send the single digit parser "2"
		 then it will return its integer value, "2"
