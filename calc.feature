Feature: testing our calculator

	Scenario: parsing a single digit number
		Given we have imported calc
		 when we send the single digit parser "2"
		 then it will return its single integer value, "2"

	Scenario: parsing a single digit number
		Given we have imported calc
		 when we send the single digit parser "3"
		 then it will return its single integer value, "3"

	Scenario: parsing a multi digit number
		Given we have imported calc
		 when we send the multi digit parser "52"
		 then it will return its multiple integer value, "52"

	Scenario: parsing a float number
		Given we have imported calc
		 when we send the float parser "1.125"
		 then it will return its float value, "1.125"

	Scenario: parsing a hex digit
		Given we have imported calc
		 when we send the single hex parser "F"
		 then it will return its hex value, "15"

	Scenario: parsing a multi hex number
		Given we have imported calc
		 when we send the full hex parser "F15A4"
		 then it will return its multi hex value, "988580"
