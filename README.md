# Structural-Engineering-Wall-Footings-Reinforced-Concrete-
A program that helps in designing reinforced concrete wall footings to carry a wall (masonry or concrete) in Structural Engineering

This program calculates and aims to help in designing normal-weight reinforced concrete wall footings to support a wall (can be masonry or concrete) in subject of Reinforced Concrete in the field of Structural Engineering, while following ACI code requirements. Different types of conditions might have impact on the overall design, so user is allowed to input values of given conditions. Also, because designing a wall footing requires not only just following the requirements, but also user's preference, therefore, this program allows some user-interactions.

Assumptions:
* Design considers a typical 12-in-wide strip along the length of wall (ACI);
for calculations: wall width= 12 in or 1 ft.
* Weight of earth on top of footing (soil)=100 psf
* Unless specified in the problem, assumed footing thickness should anywhere 1 to 1.5 of wall thickness (ACI): (need user input)
* Width of footing is equal to area of footing since the other dimension is 1 ft
* phi=0.9 (Tension control)



Input:
* service loads(dead and live)
* fc and fy values in psi
* allowable soil pressure in ksf
* initial assumption of footing thickness
* Distance between the bottom of footing to the finished ground line
* assumed bar number for calculating effective depth (initially)
* wall types (masonry or concrete)
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

* initiate by input values for :
* Service dead and live loads in kip-ft
* fc and fy in f_c_psi
* weight of earth (assumed to be 100 pcf)
* allowable soil pressure in ksf
* Distance between footing bottom and ground in ft
* assumed footing thickness (initial) in in.
* bar assumption ( can be #3-#11)

* Later in the calculations also input:
* wall type into function momentCS
* Design of tension steel and longitudinal steel: enter the corresponding user preference from the list of areas available that Satisfy the ACI
* reinforcement location, coating, and reinforcement size factors for the development length

* The program will then help calculate results for initial calculations, shear, check for adequacy, moment, areas of steel(tension as well as longitudinal), development length. It will provide design options(already satisfy ACI) for the steel reinforcement, and user can choose any preferred from the list.  
