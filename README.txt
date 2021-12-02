1) DESCRIPTION:
This application displays a choropleth map of the real estate capitalization rates on a county level for the United States.
The interactive choropleth map allows users to plug in their own assumptions and preferences in order to tailor the calculation
to factors which are most pertinent to the user. The calculations are also done on a county level, which is more granular than
currently available tools. For investors, features were added so that the user can filter by average rent rate, which is differentiated
by the number of bedrooms the property has. The resulting visualization takes into account user inputs (mortgage, ownership costs)
as well as publicly available data (crime rate, natural disaster risk, average insurance costs).

To create the application, we used the python flask framework to host the application. We have used python to parse and prepare
the CSV files and scraped data files. We then take the data and pass it to client side to be calculated and displayed. On the client
side, we use UI rich libraries such as jquery, bootstrap, D3 and MathJax to show the choropleth map, the customizable calculations,
and the data insights section where we display a bar chart of the cost break down, the calculation formula, and the information of
the clicked county.

2) INSTALLATION:
Setup:
1) Make sure you have miniconda installed in your local computer
2) run the following commands:
conda create -n dvfp python=3.6
conda activate dvfp
pip install flask
pip install pandas

3) EXECUTION
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
