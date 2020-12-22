from source import Structural_footing

# For the problem solving:
# Given information:
# wall_width_ft=1
# service_DeadLoad_kft=10
# service_LiveLoad_kft=20
# f_c_psi=3000
# f_y=60000
# w_e_lbperft3=100
# allowable_soil_press_ksf=5
# ftgBottom_BelowGround_ft=4
# wall_type= masonry
# assumed_FTG_thickness_in=18
# bar_assumption=8
stru=Structural_footing(1,100,18,10,20,3000,60000,5,4,8,'masonry')
print(stru)
print([stru.AS_available()])
design_for_steel=stru.design()
print([stru.AS_longitudinal_available()])
design_for_longitudinal=stru.design_longitudinal()
# To use the class Structural footing:
# assigned variable=Structural_footing(wall_width_ft, w_e_lbperft3, assumed_FTG_thickness_in, service_DeadLoad_kft, service_LiveLoad_kft, f_c_psi, f_y, allowable_soil_press_ksf, ftgBottom_BelowGround_ft, bar_assumption, wall_type)
# The program will first ask user to input values of f_y and f_c_psi
# I put in 60000 for f_y (first input) and 3000 for f_c_psi (second input).
# Then it will get excecuted further and return a list of available options of designing steel
# Pick a tuple: I picked (6,9) and input the first value 6 into the bar number(first input) and 9 into the bar spacing (second input)
# The program will return a statement with the design chosen and also provide the corresponding area of steel from the table
# my result: Use No. 6  at  9 in.oc. (As =  0.59 in^2).
# Then it will return a second list of available options of designing longitudinal steel
# Pick a tuple: I picked (5,9) and input the first value 5 into the bar number (first input) and 9 into the number of bars (second input)
# The program will return a statement with the design chosen and also provide the corresponding area of steel from the table
# my result: Use  9  No.  5  bars (As =  2.79 in^2) spaced equally
# overall excecution time:  20.521 s
