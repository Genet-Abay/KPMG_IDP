# KPMG Document processing


* PDf to text

	how and what we have used

* Language spliting
    
	What techniques used
	
* Mining text

   key word search and summarization
	
* Analysis and Dashboard

   what tools we have used and what we got and the dashboard here
 

## Prerequisites
 
If docker is used all requred libraries will be handled by docker. If app.py is used NumPy, Pandas, scikit-learn and python 3.10 are requred.
 
 
## Usage
Crate docker image from docker file and run the docker image to use the application. 

Building docker image

    docker build -t realestatepriceprediction
	
Running docker image

    docker run -d -p 80:80 realestatepriceprediction
	
It can also be used by running app.py in the deployment folder.
	
	```
	> python3 /deployment/app.py 

	OR

	> python /deployment/app.py 

	OR

	> py /deployment/app.py 		
	```
      
Test the API
    localhost:80/prediction
	
	
## Input
 
Input  is pdf file 
 
## Output
  
Inriched database and CSV file containing ...
		
		
		
## License

Free license

## Contact

Genet Abay Shiferaw: genetabay.s@gmail.com

Abdulhamid Albaz: a.hamidelbaz@gmail.com

Beatrice  :  beavdv2000@gmail.com

Repository link : https://github.com/Genet-Abay/real-estate-price-prediction

## Acknowledgments

BeCode Arai4 AI coaches(Chrysanthi and Louis)