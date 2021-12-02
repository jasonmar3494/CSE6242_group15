Description: This application displays a choropleth map of the real estate capitalization rates on a county level for the United States. The resulting visualization takes into account user inputs (mortgage, ownership costs) as well as publicly available data (crime rate, natural disaster risk, average insurance costs). The user is able to dig deeper per county and see relevant information pertaining to the cost breakdown.


Setup:
1) Make sure you have miniconda installed in your local computer
2) run the following commands:
conda create -n dvfp python=3.6
conda activate dvfp
pip install flask
pip install pandas

How to run:
1) Make sure you are in the correct env. Run: conda activate dvfp
2) python MainServer.py
3) Go to your browser and navigate to: http://127.0.0.1:5000/

Datasets used:
	- FHFA House Price Index : https://www.fhfa.gov/DataTools/Downloads/Pages/House-Price-Index.aspx
	- US HUD PD&R Rental Index : https://www.huduser.gov/portal/datasets/50per.html
	- Crime Data by City : https://ucr.fbi.gov/crime-in-the-u.s/2010/crime-in-the-u.s.-2010/tables/10tbl08.xls/view
	- FEMA Natural Disaster Risk : https://hazards.fema.gov/nri/data-resources\
	- Flood Insurance : https://quotewizard.com/home-insurance/average-cost-of-flood-insurance
	- Earthquake Insurance : https://www.coverage.com/insurance/home/earthquake-insurance/
	- Homeowners Insurance : https://www.insurance.com/home-and-renters-insurance/home-insurance-basics/average-homeowners-insurance-rates-by-state
