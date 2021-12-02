
// cap rate = net operation income / current market value
// Net operating income = property income - cost of ownership
function calcCapRate(region_data, input_data) {
	// console.log("calcCapRate region_data", region_data);
	// console.log("calcCapRate input_data", input_data);

	// Current Market Value = housing price index
	var curr_market_val = region_data.properties.hpi;
	// console.log("current market value", curr_market_val);

	// Property Income = Rental price index
	var rental_rate_list = [region_data.properties.rent_0,region_data.properties.rent_1,region_data.properties.rent_2,region_data.properties.rent_3,region_data.properties.rent_4]
	selected_rental_rate = rental_rate_list[input_data.rent_br]
	var prop_income = selected_rental_rate * 12;
	// console.log("property income", prop_income);

	// insurance costs = (flood x P(flood)) + (HOA x P(Tornado, Fire, Hurricane, Crime))
	var insurance_cost = region_data.properties.insurance_cost;

	// Cost of Ownership = property tax + mortgage + average maintenance cost + forecasted maintenance expenses + insurance costs
	var cost_of_ownership = region_data.properties.cost_of_ownership;

	var net_operating_income = prop_income - cost_of_ownership;

	var cap_rate = (net_operating_income / curr_market_val) * 100;
	// console.log("cap_rate", cap_rate);

	return cap_rate;
}