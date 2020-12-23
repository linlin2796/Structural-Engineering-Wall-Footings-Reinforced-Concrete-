# Structural-Engineering-Wall-Footings-Reinforced-Concrete-
A program that helps in designing reinforced concrete wall footings to carry a wall (masonry or concrete) in Structural Engineering

This program calculates and aims to help in designing normal-weight reinforced concrete wall footings to support a wall (can be masonry or concrete) in subject of Reinforced Concrete in the field of Structural Engineering, while following ACI code requirements. Different types of conditions might have impact on the overall design, so user is allowed to input values of given conditions. Also, because designing a wall footing requires not only just following the requirements, but also user's preference, therefore, this program allows some user-interactions.

Assumptions:
* Design considers a typical 12-in-wide strip along the length of wall (ACI);
for calculations: wall width= 12 in or 1 ft.
* Weight of earth on top of footing (soil)=100 psf
* Unless specified in the problem, assumed footing thickness should anywhere 1 to 1.5 of wall thickness (ACI).
* Width of footing is equal to area of footing since the other dimension is 1 ft
* phi=0.9 (Tension control)


Input:
* wall width in feet (ACI recommended 1ft, also under Assumptions)
* weight of earth, soil (usually use 100 psf, ACI)
* service loads in k-ft (dead and live)
* fc and fy values in psi
* allowable soil pressure in ksf
* initial assumption of footing thickness
* Distance between the bottom of footing to the finished ground line
* assumed bar number for calculating effective depth (initially)
* wall type (masonry or concrete)
* design preferences (after using tables)

Output:
* Results of preliminary calculations
* shear and shear check (adequacy of the assumed footing thickness)
* moment
* Design of tension steel, longitudinal steel
* development length calculation and check

## Setup
In order to use the program, you have to clone/download this repository, navigate to the local directory and create a virtual environment with:

```
$ python3 -m venv venv

```
Then, activate the virtual environment:

```
For Linux/Mac OS:
$ source venv/bin/activate

For Windows:
> venv\Scripts\activate
```

Finally, install the required libraries for this program with:

```
$ pip install -r requirements.txt

```

## This is how to use the program
![image](https://user-images.githubusercontent.com/73927161/102945154-f4502200-448a-11eb-88d5-c93b44916045.png)


Here is how we can solve and design the wall footing for the problem above.
First, instantiate a new object of Structural_footing by following the format below:
![image](https://user-images.githubusercontent.com/73927161/102944790-d209d480-4489-11eb-902e-791442b5c9c4.png)
* initiate by input values for :
* wall width in ft
* weight of earth (100 pcf)
* assumed footing thickness (initial) in in.
* Service dead and live loads in kip-ft
* fc and fy in f_c_psi
* allowable soil pressure in ksf
* Distance between footing bottom and ground in ft
* bar assumption (can be #3 - #11, ACI recommended #8)
* wall type (masonry or concrete)

Finally we can solve and print the results:
![image](https://user-images.githubusercontent.com/73927161/102952223-afcd8200-449c-11eb-932a-b303486c53b6.png)
############# Must read 
***Note for the output (if not sure, please check test.py for example):
* The program will first need user to input values of f_y and f_c_psi once more: remember that f_y is either 40000 or 60000, and f_c_psi is 3000,4000, or 5000  (provided by the problem). For f_y=40000, the options of f_c_psi are 3000 and 4000. For f_y=60000, the options of f_c_psi are 3000,4000, and 5000. This is required by the use of tables.

* The program will then return results for shear, shear check, moment

* Then, it will return a list of available options for area of steel for user to pick for designing
* User needs to choose a tuple from the list, and input the bar number (first number of tuple) into the first input, press enter, and input the bar spacing (second number of tuple) into the second input
* Program returns a statement with the chosen design of steel and the corresponding area of steel from table

* Then, it will return a request for user to input their design once more for calculating the development length. Please enter the bar number and bar spacing again in the inputs. Example is shown in Test.py
* Program returns development length and adequacy check

* Then, it will return a list of available options for area of longitudinal steel for user to pick for designing
* User needs to choose a tuple from the list, and input the bar number (first number of tuple) into the first input, press enter, and input number of bars (second number of tuple) into the second input.

* An image of Output from example in test.py is shown below:
![image](https://user-images.githubusercontent.com/73927161/102952064-451c4680-449c-11eb-824a-917e71155fb6.png)
More details are provided in test.py
