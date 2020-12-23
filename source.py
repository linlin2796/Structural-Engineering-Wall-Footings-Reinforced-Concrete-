# imports
import numpy as np


## Tables as Dictionaries

#bar#:(Diameter, Area)
TableA1={3:[0.375,0.11], 4:[0.500,0.20], 5:[0.625, 0.31], 6:[0.750,0.44], 7:[0.875,0.60], 8:[1.000,0.79], 9:[1.128,1.00], 10:[1.270,1.27], 11:[1.410,1.56], 14:[1.693,2.25], 18:[2.257,4.00]}

#(bar#,# of bar):area
TableA2={(3,1):0.11, (3,2):0.22, (3,3):0.33, (3,4):0.44, (3,5):0.55, (3,6):0.66, (3,7):0.77, (3,8):0.88, (3,9):0.99, (3,10):1.10, (3,11):1.21, (3,12):1.32, (3,13):1.43, (3,14):1.54, (3,15):1.65, (3,16):1.76, (3,17):1.87, (3,18):1.98, (3,19):2.09, (3,20):2.20,
         (4,1):0.20, (4,2):0.40, (4,3):0.60, (4,4):0.80, (4,5):1.00, (4,6):1.20, (4,7):1.40, (4,8):1.60, (4,9):1.80, (4,10):2.00, (4,11):2.20, (4,12):2.40, (4,13):2.60, (4,14):2.80, (4,15):3.00, (4,16):3.20, (4,17):3.40, (4,18):3.60, (4,19):3.80, (4,20):4.00,
         (5,1):0.31, (5,2):0.62, (5,3):0.93, (5,4):1.24, (5,5):1.55, (5,6):1.86, (5,7):2.17, (5,8):2.48, (5,9):2.79, (5,10):3.10, (5,11):3.41, (5,12):3.72, (5,13):4.03, (5,14):4.34, (5,15):4.65, (5,16):4.96, (5,17):5.27, (5,18):5.58, (5,19):5.89, (5,20):6.20,
         (6,1):0.44, (6,2):0.88, (6,3):1.32, (6,4):1.76, (6,5):2.20, (6,6):2.64, (6,7):3.08, (6,8):3.52, (6,9):3.96, (6,10):4.40, (6,11):4.84, (6,12):5.28, (6,13):5.72, (6,14):6.16, (6,15):6.60, (6,16):7.04, (6,17):7.48, (6,18):7.92, (6,19):8.36, (6,20):8.80,
         (7,1):0.60, (7,2):1.20, (7,3):1.80, (7,4):2.40, (7,5):3.00, (7,6):3.60, (7,7):4.20, (7,8):4.80, (7,9):5.40, (7,10):6.00, (7,11):6.60, (7,12):7.20, (7,13):7.80, (7,14):8.40, (7,15):9.00, (7,16):9.60, (7,17):10.2, (7,18):10.8, (7,19):11.4, (7,20):12.0,
         (8,1):0.79, (8,2):1.58, (8,3):2.37, (8,4):3.16, (8,5):3.93, (8,6):4.74, (8,7):5.53, (8,8):6.32, (8,9):7.11, (8,10):7.90, (8,11):8.69, (8,12):9.48, (8,13):10.3, (8,14):11.1, (8,15):11.8, (8,16):12.6, (8,17):13.4, (8,18):14.2, (8,19):15.0, (8,20):15.8,
         (9,1):1.00, (9,2):2.00, (9,3):3.00, (9,4):4.00, (9,5):5.00, (9,6):6.00, (9,7):7.00, (9,8):8.00, (9,9):9.00, (9,10):10.0, (9,11):11.0, (9,12):12.0, (9,13):13.0, (9,14):14.0, (9,15):15.0, (9,16):16.0, (9,17):17.0, (9,18):18.0, (9,19):19.0, (9,20):20.0,
         (10,1):1.27,(10,2):2.54,(10,3):3.81,(10,4):5.08,(10,5):6.35,(10,6):7.62,(10,7):8.89,(10,8):10.2,(10,9):11.4,(10,10):12.7,(10,11):14.0,(10,12):15.2,(10,13):16.5,(10,14):17.8,(10,15):19.0,(10,16):20.3,(10,17):21.6,(10,18):22.9,(10,19):24.1,(10,20):25.4,
         (11,1):1.56,(11,2):3.12,(11,3):4.68,(11,4):6.24,(11,5):7.80,(11,6):9.36,(11,7):10.9,(11,8):12.5,(11,9):14.0,(11,10):15.6,(11,11):17.2,(11,12):18.7,(11,13):20.3,(11,14):21.8,(11,15):23.4,(11,16):25.0,(11,17):26.5,(11,18):28.1,(11,19):29.6,(11,20):31.2
 }

 # (bar#,spacing):area
TableA4={(3,2):0.66, (3,2.5):0.53, (3,3):0.44, (3,3.5):0.38, (3,4):0.33, (3,4.5):0.29, (3,5):0.26, (3,5.5):0.24, (3,6):0.22, (3,6.5):0.20, (3,7):0.19, (3,7.5):0.18, (3,8):0.16, (3,9):0.15, (3,10):0.13, (3,11):0.12, (3,12):0.11, (3,13):0.10, (3,14):0.09, (3,15):0.09, (3,16):0.08, (3,17):0.08, (3,18):0.07,
         (4,2):1.20, (4,2.5):0.96, (4,3):0.80, (4,3.5):0.69, (4,4):0.60, (4,4.5):0.53, (4,5):0.48, (4,5.5):0.44, (4,6):0.40, (4,6.5):0.37, (4,7):0.34, (4,7.5):0.32, (4,8):0.30, (4,9):0.27, (4,10):0.24, (4,11):0.22, (4,12):0.20, (4,13):0.18, (4,14):0.17, (4,15):0.16, (4,16):0.15, (4,17):0.14, (4,18):0.13,
         (5,2):1.86, (5,2.5):1.49, (5,3):1.24, (5,3.5):1.06, (5,4):0.93, (5,4.5):0.83, (5,5):0.74, (5,5.5):0.68, (5,6):0.62, (5,6.5):0.57, (5,7):0.53, (5,7.5):0.50, (5,8):0.46, (5,9):0.41, (5,10):0.37, (5,11):0.34, (5,12):0.31, (5,13):0.29, (5,14):0.27, (5,15):0.25, (5,16):0.23, (5,17):0.22, (5,18):0.21,
                     (6,2.5):2.11, (6,3):1.76, (6,3.5):1.51, (6,4):1.32, (6,4.5):1.17, (6,5):1.06, (6,5.5):0.96, (6,6):0.88, (6,6.5):0.81, (6,7):0.75, (6,7.5):0.70, (6,8):0.66, (6,9):0.59, (6,10):0.53, (6,11):0.48, (6,12):0.44, (6,13):0.41, (6,14):0.38, (6,15):0.35, (6,16):0.33, (6,17):0.31, (6,18):0.29,
                                   (7,3):2.40, (7,3.5):2.06, (7,4):1.80, (7,4.5):1.60, (7,5):1.44, (7,5.5):1.31, (7,6):1.20, (7,6.5):1.11, (7,7):1.03, (7,7.5):0.96, (7,8):0.90, (7,9):0.80, (7,10):0.72, (7,11):0.65, (7,12):0.60, (7,13):0.55, (7,14):0.51, (7,15):0.48, (7,16):0.45, (7,17):0.42, (7,18):0.40,
                                   (8,3):3.16, (8,3.5):2.71, (8,4):2.37, (8,4.5):2.11, (8,5):1.90, (8,5.5):1.72, (8,6):1.58, (8,6.5):1.46, (8,7):1.35, (8,7.5):1.26, (8,8):1.18, (8,9):1.05, (8,10):0.95, (8,11):0.86, (8,12):0.79, (8,13):0.73, (8,14):0.68, (8,15):0.64, (8,16):0.59, (8,17):0.56, (8,18):0.53,
                                   (9,3):4.00, (9,3.5):3.43, (9,4):3.00, (9,4.5):2.67, (9,5):2.40, (9,5.5):2.18, (9,6):2.00, (9,6.5):1.85, (9,7):1.71, (9,7.5):1.60, (9,8):1.50, (9,9):1.33, (9,10):1.20, (9,11):1.09, (9,12):1.00, (9,13):0.92, (9,14):0.86, (9,15):0.80, (9,16):0.75, (9,17):0.71, (9,18):0.67,
                                              (10,3.5):4.35,(10,4):3.81,(10,4.5):3.39,(10,5):3.05,(10,5.5):2.77,(10,6):2.54,(10,6.5):2.34,(10,7):2.18,(10,7.5):2.03,(10,8):1.90,(10,9):1.69,(10,10):1.52,(10,11):1.39,(10,12):1.27,(10,13):1.17,(10,14):1.09,(10,15):1.02,(10,16):0.95,(10,17):0.90,(10,18):0.85,
                                                            (11,4):4.68,(11,4.5):4.16,(11,5):3.74,(11,5.5):3.40,(11,6):3.12,(11,6.5):2.88,(11,7):2.67,(11,7.5):2.50,(11,8):2.34,(11,9):2.08,(11,10):1.87,(11,11):1.70,(11,12):1.56,(11,13):1.44,(11,14):1.34,(11,15):1.25,(11,16):1.17,(11,17):1.10,(11,18):1.04
}

# (fy,fc):min
TableA5={(40000,3000):0.0050, (40000,4000):0.0050, (40000,5000):0.0053, (40000,6000):0.0058,
         (50000,3000):0.0040, (50000,4000):0.0040, (50000,5000):0.0042, (50000,6000):0.0046,
         (60000,3000):0.0033, (60000,4000):0.0033, (60000,5000):0.0035, (60000,6000):0.0039,
         (75000,3000):0.0027, (75000,4000):0.0027, (75000,5000):0.0028, (75000,6000):0.0031
         }

#Assume tension controls Et>0.005, phi=0.9 is correct
# for fc=3,000 psi, fy=40,000 psi, kbar in ksi
#kbar:rho
TableA7={0.0397:0.0010, 0.0436:0.0011, 0.0476:0.0012, 0.0515:0.0013, 0.0554:0.0014, 0.0593:0.0015, 0.0632:0.0016, 0.0671:0.0017, 0.0710:0.0018, 0.0749:0.0019, 0.0788:0.0020, 0.0826:0.0021, 0.0865:0.0022, 0.0903:0.0023, 0.0942:0.0024, 0.0980:0.0025, 0.1019:0.0026, 0.1057:0.0027, 0.1095:0.0028, 0.1134:0.0029, 0.1172:0.0030, 0.1210:0.0031, 0.1248:0.0032, 0.1286:0.0033, 0.1324:0.0034, 0.1362:0.0035, 0.1399:0.0036, 0.1437:0.0037, 0.1475:0.0038, 0.1512:0.0039, 0.1550:0.0040, 0.1587:0.0041, 0.1625:0.0042, 0.1662:0.0043, 0.1699:0.0044, 0.1736:0.0045, 0.1774:0.0046, 0.1811:0.0047, 0.1848:0.0048, 0.1885:0.0049, 0.1922:0.0050, 0.1958:0.0051, 0.1995:0.0052, 0.2032:0.0053,
         0.2069:0.0054, 0.2105:0.0055, 0.2142:0.0056, 0.2178:0.0057, 0.2214:0.0058, 0.2251:0.0059, 0.2287:0.0060, 0.2323:0.0061, 0.2359:0.0062, 0.2395:0.0063, 0.2431:0.0064, 0.2467:0.0065, 0.2503:0.0066, 0.2539:0.0067, 0.2575:0.0068, 0.2611:0.0069, 0.2646:0.0070, 0.2682:0.0071, 0.2717:0.0072, 0.2753:0.0073, 0.2788:0.0074, 0.2824:0.0075, 0.2859:0.0076, 0.2894:0.0077, 0.2929:0.0078, 0.2964:0.0079, 0.2999:0.0080, 0.3034:0.0081, 0.3069:0.0082, 0.3104:0.0083, 0.3139:0.0084, 0.3173:0.0085, 0.3208:0.0086, 0.3243:0.0087, 0.3277:0.0088, 0.3311:0.0089, 0.3346:0.0090, 0.3380:0.0091, 0.3414:0.0092, 0.3449:0.0093, 0.3483:0.0094, 0.3517:0.0095, 0.3551:0.0096, 0.3585:0.0097,
         0.3619:0.0098, 0.3653:0.0099, 0.3686:0.0100, 0.3720:0.0101, 0.3754:0.0102, 0.3787:0.0103, 0.3821:0.0104, 0.3854:0.0105, 0.3887:0.0106, 0.3921:0.0107, 0.3954:0.0108, 0.3987:0.0109, 0.4020:0.0110, 0.4053:0.0111, 0.4086:0.0112, 0.4119:0.0113, 0.4152:0.0114, 0.4185:0.0115, 0.4218:0.0116, 0.4251:0.0117, 0.4283:0.0118, 0.4316:0.0119, 0.4348:0.0120, 0.4381:0.0121, 0.4413:0.0122, 0.4445:0.0123, 0.4478:0.0124, 0.4510:0.0125, 0.4542:0.0126, 0.4574:0.0127, 0.4606:0.0128, 0.4638:0.0129, 0.4670:0.0130, 0.4702:0.0131, 0.4733:0.0132, 0.4765:0.0133, 0.4797:0.0134, 0.4828:0.0135, 0.4860:0.0136, 0.4891:0.0137, 0.4923:0.0138, 0.4954:0.0139, 0.4985:0.0140, 0.5016:0.0141,
         0.5047:0.0142, 0.5981:0.0173, 0.6836:0.02033

}

#Assume tension controls Et>0.005, phi=0.9 is correct
# for fc=3,000 psi, fy=60,000 psi, kbar in ksi
#kbar:rho
TableA8={0.0593:0.0010, 0.0651:0.0011, 0.0710:0.0012, 0.0768:0.0013, 0.0826:0.0014, 0.0884:0.0015, 0.0942:0.0016, 0.1000:0.0017, 0.1057:0.0018, 0.1115:0.0019, 0.1172:0.0020, 0.1229:0.0021, 0.1286:0.0022, 0.1343:0.0023, 0.1399:0.0024, 0.1456:0.0025, 0.1512:0.0026, 0.1569:0.0027, 0.1625:0.0028, 0.1681:0.0029, 0.1736:0.0030, 0.1792:0.0031, 0.1848:0.0032, 0.1903:0.0033, 0.1958:0.0034, 0.2014:0.0035, 0.2069:0.0036, 0.2123:0.0037, 0.2178:0.0038,
         0.3294:0.0059, 0.3346:0.0060, 0.3397:0.0061, 0.3449:0.0062, 0.3500:0.0063, 0.3551:0.0064, 0.3602:0.0065, 0.3653:0.0066, 0.3703:0.0067, 0.3754:0.0068, 0.3804:0.0069, 0.3854:0.0070, 0.3904:0.0071, 0.3954:0.0072, 0.4004:0.0073, 0.4054:0.0074, 0.4103:0.0075, 0.4152:0.0076, 0.4202:0.0077, 0.4251:0.0078, 0.4300:0.0079, 0.4348:0.0080, 0.4397:0.0081, 0.4446:0.0082, 0.4494:0.0083, 0.4542:0.0084, 0.4590:0.0085, 0.4638:0.0086, 0.4686:0.0087,
         0.5657:0.0108, 0.5702:0.0109, 0.5746:0.0110, 0.5791:0.0111, 0.5835:0.0112, 0.5879:0.0113, 0.5923:0.0114, 0.5967:0.0115, 0.6011:0.0116, 0.6054:0.0117, 0.6098:0.0118, 0.6141:0.0119, 0.6184:0.0120, 0.6227:0.0121, 0.6270:0.0122, 0.6312:0.0123, 0.6355:0.0124, 0.6398:0.0125, 0.6440:0.0126, 0.6482:0.0127, 0.6524:0.0128, 0.6566:0.0129, 0.6608:0.0130, 0.6649:0.0131, 0.6691:0.0132, 0.6732:0.0133, 0.6773:0.0134, 0.6814:0.0135, 0.6835:0.01355
}

#Assume tension controls Et>0.005, phi=0.9 is correct
# for fc=4,000 psi, fy=40,000 psi, kbar in ksi
#kbar:rho
TableA9={0.0398:0.0010, 0.0437:0.0011, 0.0477:0.0012, 0.0516:0.0013, 0.0555:0.0014, 0.0595:0.0015, 0.0634:0.0016, 0.0673:0.0017, 0.0712:0.0018, 0.0752:0.0019, 0.0791:0.0020, 0.0830:0.0021, 0.0869:0.0022, 0.0908:0.0023, 0.0946:0.0024, 0.0985:0.0025, 0.1024:0.0026, 0.1063:0.0027, 0.1102:0.0028, 0.1140:0.0029, 0.1179:0.0030, 0.1217:0.0031, 0.1256:0.0032, 0.1294:0.0033, 0.1333:0.0034, 0.1371:0.0035, 0.1410:0.0036, 0.1448:0.0037, 0.1486:0.0038, 0.1524:0.0039, 0.1562:0.0040, 0.1600:0.0041, 0.1638:0.0042, 0.1676:0.0043, 0.1714:0.0044, 0.1752:0.0045, 0.1790:0.0046, 0.1828:0.0047, 0.1866:0.0048, 0.1904:0.0049, 0.1941:0.0050, 0.1979:0.0051, 0.2016:0.0052, 0.2054:0.0053,
         0.2091:0.0054, 0.2129:0.0055, 0.2166:0.0056, 0.2204:0.0057, 0.2241:0.0058, 0.2278:0.0059, 0.2315:0.0060, 0.2352:0.0061, 0.2390:0.0062, 0.2427:0.0063, 0.2464:0.0064, 0.2501:0.0065, 0.2538:0.0066, 0.2574:0.0067, 0.2611:0.0068, 0.2648:0.0069, 0.2685:0.0070, 0.2721:0.0071, 0.2758:0.0072, 0.2795:0.0073, 0.2831:0.0074, 0.2868:0.0075, 0.2904:0.0076, 0.2941:0.0077, 0.2977:0.0078, 0.3013:0.0079, 0.3049:0.0080, 0.3086:0.0081, 0.3122:0.0082, 0.3158:0.0083, 0.3194:0.0084, 0.3230:0.0085, 0.3266:0.0086, 0.3302:0.0087, 0.3338:0.0088, 0.3374:0.0089, 0.3409:0.0090, 0.3445:0.0091, 0.3481:0.0092, 0.3517:0.0093, 0.3552:0.0094, 0.3588:0.0095, 0.3623:0.0096, 0.3659:0.0097,
         0.3694:0.0098, 0.3729:0.0099, 0.3765:0.0100, 0.3800:0.0101, 0.3835:0.0102, 0.3870:0.0103, 0.3906:0.0104, 0.3941:0.0105, 0.3976:0.0106, 0.4011:0.0107, 0.4046:0.0108, 0.4080:0.0109, 0.4115:0.0110, 0.4150:0.0111, 0.4185:0.0112, 0.4220:0.0113, 0.4254:0.0114, 0.4289:0.0115, 0.4323:0.0116, 0.4358:0.0117, 0.4392:0.0118, 0.4427:0.0119, 0.4461:0.0120, 0.4495:0.0121, 0.4530:0.0122, 0.4564:0.0123, 0.4598:0.0124, 0.4632:0.0125, 0.4666:0.0126, 0.4701:0.0127, 0.4735:0.0128, 0.4768:0.0129, 0.4802:0.0130, 0.4836:0.0131, 0.4870:0.0132, 0.4904:0.0133, 0.4938:0.0134, 0.4971:0.0135, 0.5005:0.0136, 0.5038:0.0137, 0.5072:0.0138, 0.5105:0.0139, 0.5139:0.0140, 0.5172:0.0141,
         0.5206:0.0142, 0.5239:0.0143, 0.5272:0.0144, 0.5305:0.0145, 0.5338:0.0146, 0.5372:0.0147, 0.5405:0.0148, 0.5438:0.0149, 0.5471:0.0150, 0.5504:0.0151, 0.5536:0.0152, 0.5569:0.0153, 0.5602:0.0154, 0.5635:0.0155, 0.5667:0.0156, 0.5700:0.0157, 0.5733:0.0158, 0.5765:0.0159, 0.5798:0.0160, 0.5830:0.0161, 0.5863:0.0162, 0.5895:0.0163, 0.5927:0.0164, 0.5959:0.0165, 0.5992:0.0166, 0.6024:0.0167, 0.6056:0.0168, 0.6088:0.0169, 0.6120:0.0170, 0.6152:0.0171, 0.6184:0.0172, 0.6216:0.0173, 0.6248:0.0174, 0.6279:0.0175, 0.6311:0.0176, 0.6343:0.0177, 0.6375:0.0178, 0.6406:0.0179, 0.6438:0.0180, 0.6469:0.0181, 0.6501:0.0182, 0.6532:0.0183, 0.6563:0.0184, 0.6595:0.0185,
         0.6626:0.0186, 0.7927:0.0229, 0.9113:0.0271
}

#Assume tension controls Et>0.005, phi=0.9 is correct
# for fc=4,000 psi, fy=60,000 psi, kbar in ksi
#kbar:rho
TableA10={0.0595:0.0010, 0.0654:0.0011, 0.0712:0.0012, 0.0771:0.0013, 0.0830:0.0014, 0.0889:0.0015, 0.0946:0.0016, 0.1005:0.0017, 0.1063:0.0018, 0.1121:0.0019, 0.1179:0.0020, 0.1237:0.0021, 0.1294:0.0022, 0.1352:0.0023, 0.1410:0.0024, 0.1467:0.0025, 0.1524:0.0026, 0.1581:0.0027, 0.1638:0.0028, 0.1695:0.0029, 0.1752:0.0030, 0.1809:0.0031, 0.1866:0.0032, 0.1922:0.0033, 0.1979:0.0034, 0.2035:0.0035, 0.2091:0.0036, 0.2148:0.0037, 0.2204:0.0038,
          0.2259:0.0039, 0.2315:0.0040, 0.2371:0.0041, 0.2427:0.0042, 0.2482:0.0043, 0.2538:0.0044, 0.2593:0.0045, 0.2648:0.0046, 0.2703:0.0047, 0.2758:0.0048, 0.2813:0.0049, 0.2868:0.0050, 0.2922:0.0051, 0.2977:0.0052, 0.3031:0.0053, 0.3086:0.0054, 0.3140:0.0055, 0.3194:0.0056, 0.3248:0.0057, 0.3302:0.0058, 0.3356:0.0059, 0.3409:0.0060, 0.3463:0.0061, 0.3516:0.0062, 0.3570:0.0063, 0.3623:0.0064, 0.3676:0.0065, 0.3729:0.0066, 0.3782:0.0067,
          0.3835:0.0068, 0.3888:0.0069, 0.3941:0.0070, 0.3993:0.0071, 0.4046:0.0072, 0.4098:0.0073, 0.4150:0.0074, 0.4202:0.0075, 0.4254:0.0076, 0.4306:0.0077, 0.4358:0.0078, 0.4410:0.0079, 0.4461:0.0080, 0.4513:0.0081, 0.4564:0.0082, 0.4615:0.0083, 0.4666:0.0084, 0.4718:0.0085, 0.4768:0.0086, 0.4819:0.0087, 0.4870:0.0088, 0.4921:0.0089, 0.4971:0.0090, 0.5022:0.0091, 0.5072:0.0092, 0.5122:0.0093, 0.5172:0.0094, 0.5222:0.0095, 0.5272:0.0096,
          0.5322:0.0097, 0.5372:0.0098, 0.5421:0.0099, 0.5471:0.0100, 0.5520:0.0101, 0.5569:0.0102, 0.5618:0.0103, 0.5667:0.0104, 0.5716:0.0105, 0.5765:0.0106, 0.5814:0.0107, 0.5862:0.0108, 0.5911:0.0109, 0.5959:0.0110, 0.6008:0.0111, 0.6056:0.0112, 0.6104:0.0113, 0.6152:0.0114, 0.6200:0.0115, 0.6248:0.0116, 0.6296:0.0117, 0.6343:0.0118, 0.6391:0.0119, 0.6438:0.0120, 0.6485:0.0121, 0.6532:0.0122, 0.6579:0.0123, 0.6626:0.0124, 0.6673:0.0125,
          0.6720:0.0126, 0.7985:0.0154, 0.9110:0.01806

}

#Assume tension controls Et>0.005, phi=0.9 is correct
# for fc=5,000 psi, fy=60,000 psi, kbar in ksi
#kbar:rho
TableA11={0.0596:0.0010, 0.0655:0.0011, 0.0714:0.0012, 0.0773:0.0013, 0.0832:0.0014, 0.0890:0.0015, 0.0949:0.0016, 0.1008:0.0017, 0.1066:0.0018, 0.1125:0.0019, 0.1183:0.0020, 0.1241:0.0021, 0.1300:0.0022, 0.1358:0.0023, 0.1416:0.0024, 0.1474:0.0025, 0.1531:0.0026, 0.1589:0.0027, 0.1647:0.0028, 0.1704:0.0029, 0.1762:0.0030, 0.1819:0.0031, 0.1877:0.0032, 0.1934:0.0033, 0.1991:0.0034, 0.2048:0.0035, 0.2105:0.0036, 0.2162:0.0037, 0.2219:0.0038, 0.2276:0.0039, 0.2332:0.0040, 0.2389:0.0041, 0.2445:0.0042, 0.2502:0.0043, 0.2558:0.0044, 0.2614:0.0045, 0.2670:0.0046, 0.2726:0.0047,
          0.2782:0.0048, 0.2838:0.0049, 0.2894:0.0050, 0.2950:0.0051, 0.3005:0.0052, 0.3061:0.0053, 0.3117:0.0054, 0.3172:0.0055, 0.3227:0.0056, 0.3282:0.0057, 0.3338:0.0058, 0.3393:0.0059, 0.3448:0.0060, 0.3502:0.0061, 0.3557:0.0062, 0.3612:0.0063, 0.3667:0.0064, 0.3721:0.0065, 0.3776:0.0066, 0.3830:0.0067, 0.3884:0.0068, 0.3938:0.0069, 0.3992:0.0070, 0.4047:0.0071, 0.4100:0.0072, 0.4154:0.0073, 0.4208:0.0074, 0.4262:0.0075, 0.4315:0.0076, 0.4369:0.0077, 0.4422:0.0078, 0.4476:0.0079, 0.4529:0.0080, 0.4582:0.0081, 0.4635:0.0082, 0.4688:0.0083, 0.4741:0.0084, 0.4794:0.0085,
          0.4847:0.0086, 0.4899:0.0087, 0.4952:0.0088, 0.5005:0.0089, 0.5057:0.0090, 0.5109:0.0091, 0.5162:0.0092, 0.5214:0.0093, 0.5266:0.0094, 0.5318:0.0095, 0.5370:0.0096, 0.5422:0.0097, 0.5473:0.0098, 0.5525:0.0099, 0.5576:0.0100, 0.5628:0.0101, 0.5679:0.0102, 0.5731:0.0103, 0.5782:0.0104, 0.5833:0.0105, 0.5884:0.0106, 0.5935:0.0107, 0.5986:0.0108, 0.6037:0.0109, 0.6088:0.0110, 0.6138:0.0111, 0.6189:0.0112, 0.6239:0.0113, 0.6290:0.0114, 0.6340:0.0115, 0.6390:0.0116, 0.6440:0.0117, 0.6490:0.0118, 0.6540:0.0119, 0.6590:0.0120, 0.6640:0.0121, 0.6690:0.0122, 0.6739:0.0123,
          0.6789:0.0124, 0.6838:0.0125, 0.6888:0.0126, 0.6937:0.0127, 0.6986:0.0128, 0.7035:0.0129, 0.7084:0.0130, 0.7133:0.0131, 0.7182:0.0132, 0.7231:0.0133, 0.7280:0.0134, 0.7328:0.0135, 0.7377:0.0136, 0.7425:0.0137, 0.7473:0.0138, 0.7522:0.0139, 0.7570:0.0140, 0.7618:0.0141, 0.7666:0.0142, 0.7714:0.0143, 0.7762:0.0144, 0.7810:0.0145, 0.7857:0.0146, 0.7905:0.0147, 0.7952:0.0148, 0.8000:0.0149, 0.8047:0.0150, 0.8094:0.0151, 0.8142:0.0152, 0.8189:0.0153, 0.8236:0.0154, 0.8283:0.0155, 0.8329:0.0156, 0.8376:0.0157, 0.8423:0.0158, 0.8469:0.0159, 0.8516:0.0160, 0.8562:0.0161,
          0.8609:0.0162, 1.0047:0.0194, 1.0838:0.02125
}

#(fy,fc):K_D
Table5_1={(40000,3000):54.8,(40000,4000):47.4,(40000,5000):42.4,(40000,6000):38.7,
          (50000,3000):68.5,(50000,4000):59.3,(50000,5000):53.0,(50000,6000):48.4,
          (60000,3000):82.2,(60000,4000):71.2,(60000,5000):63.6,(60000,6000):58.1,
         (75000,3000):102.7,(75000,4000):88.9,(75000,5000):79.5,(75000,6000):72.6

}


class Structural_footing:
    # When executing, need to first input the given value of f_y and f_c_psi in units of psi for purpose of finding reference table for later calculations.
    print("Please first enter given value of f_y, can either be 40000 psi or 60000 psi:")
    f_y=int(input())
    print("Please also enter given value of f_c_psi. For f_y=40000 psi, possible values of f_c_psi are 3000 psi and 4000 psi. For f_y=60000 psi, possible values of f_c_psi are 3000 psi ,4000 psi, and 5000 psi:")
    f_c_psi=int(input())
    def __init__(self,wall_width_ft=1,w_e_lbperft3=100,assumed_FTG_thickness_in=None,service_DeadLoad_kft=None,service_LiveLoad_kft=None, f_c_psi=f_c_psi, f_y=f_y,allowable_soil_press_ksf=None, ftgBottom_BelowGround_ft=None,bar_assumption=None,wall_type=['masonry,concrete']):
        """ This is the initiation of the class Structural_footing by inputting the neccessary initial values given by
    the problem.
    * wall width in feet: wall_width_ft (ACI:assumed 1)
    * weight of earth on(soil) top of footing in lb/ft^3: w_e_lbperft3 (ACI: usually use 100)
    * initially assumed footing thickness in inches: assumed_FTG_thickness_in (ACI: usually can be anywhere between 1-1.5 * wall width (which is 1ft =12 inches))
    * service dead load in k-ft: service_DeadLoad_kft (given by problem)
    * service live load in k-ft: service_LiveLoad_kft (given by problem)
    * fc in psi: f_c_psi (given by problem)
    * fy in psi: f_y (given by problem)
    * allowable soil pressure in ksf: allowable_soil_press_ksf (given by problem)
    * distance from footing bottom to the ground in feet: ftgBottom_BelowGround_ft (given by problem)
    * initial assumption of bar number to use: bar_assumption (can be a guess from user, but ACI usually recommend bar number 8, so can input 8)
    * wall type (masonry or concrete, type as string): wall_type (given by problem)"""
        self.wall_width_ft=wall_width_ft
        self.w_e_lbperft3=w_e_lbperft3
        self.assumed_FTG_thickness_in=assumed_FTG_thickness_in
        self.service_DeadLoad_kft=service_DeadLoad_kft
        self.service_LiveLoad_kft=service_LiveLoad_kft
        self.f_c_psi=f_c_psi
        self.f_y=f_y
        self.allowable_soil_press_ksf=allowable_soil_press_ksf
        self.ftgBottom_BelowGround_ft=ftgBottom_BelowGround_ft
        self.bar_assumption=bar_assumption
        self.wall_type=wall_type


    def table_of_reference(self):
        """ This function finds the appropriate table for reference according the input values of f_y and f_c_psi previously"""
        if self.f_y==40000 and self.f_c_psi==3000:
            return dict(TableA7)
        elif self.f_y==40000 and self.f_c_psi==4000:
            return dict(TableA9)
        elif self.f_y==60000 and self.f_c_psi==3000:
            return dict(TableA8)
        elif self.f_y==60000 and self.f_c_psi==4000:
            return dict(TableA10)
        elif self.f_y==60000 and self.f_c_psi==5000:
            return dict(TableA11)
        else:
            print("Please enter a value of f_c_psi")


    def service_load(self):
        """ This function calculates the service load given service dead load and live load"""
        return self.service_DeadLoad_kft+self.service_LiveLoad_kft


    def factored_load(self):
        """ This function calculates the factored load given service dead load and live load"""
        return 1.2*self.service_DeadLoad_kft+1.6*self.service_LiveLoad_kft


    def footing_weight(self,assumed_FTG_thickness_in):
        """ This function calculates the footing weight given the assumed footing thickness and using the ACI value for weight of normal concrete"""
        if self.assumed_FTG_thickness_in:
            return 0.150*(self.assumed_FTG_thickness_in/12)


    def depth_earth(self):
        """ This function calculates the depth of earth given the distance of footing bottom to the ground and the assumed footing thickness"""
        return (self.ftgBottom_BelowGround_ft)*12-self.assumed_FTG_thickness_in


    def earth_weight(self):
        """ This function calculates the weight of earth based on the depth of earth calculated previously and the weight of soil provided before"""
        return (self.depth_earth()*self.w_e_lbperft3)/(12*1000)


    def net_soil_press(self):
        """ This function calculates the net soil pressure based on the allowable soil pressure provided by the problem, footing weight and earth weight calculated previously, and the assumed thickness of footing"""
        return self.allowable_soil_press_ksf-self.footing_weight(self.assumed_FTG_thickness_in)-self.earth_weight()


    def req_FTG_width(self):
        """ This function calculates the required footing width, based on the service load and net soil pressure calculated previously"""
        return self.service_load()/self.net_soil_press()


    def use_FTG_width(self):
        """This function calculates the footing width user can use for calculation after determining the required footing width in the previous function"""
        return round(np.round((self.req_FTG_width()*12))/12,2)


    def factoredSoilPress_ksf(self):
        """This function calculates the factored soil pressure in ksf based on the factored load and the footing width used"""
        return self.factored_load()/self.use_FTG_width()


    def bar_diameter(self):
        """This function helps user find the bar diameter from table corresponding to the bar number assumed previously"""
        return TableA1[self.bar_assumption][0]


    def assumed_effective_depth(self):
        """This function calculates the assumed effective depth based on the assumed footing thickness and the diameter of the bar assumed"""
        return self.assumed_FTG_thickness_in-3-0.5*self.bar_diameter()


    def shear_Vu_(self):
        """This function calculates the shear based on the footing width used, wall width, and assumed effective depth"""
        L=0.5*(self.use_FTG_width()-self.wall_width_ft)-(self.assumed_effective_depth()/12)
        return self.factoredSoilPress_ksf()*np.round(L,2)


    def shear_strength_phiVc(self):
        """This function finds the available shear strength based on the f_c_psi, wall width, and assumed effective depth"""
        return (0.75*2*np.sqrt(self.f_c_psi)*(self.wall_width_ft*12)*(self.assumed_effective_depth()))/1000


    def shear_check(self):
        """ This function checks whether calculated shear is less than the available shear, which determines whether if the assumed thickness of footing satisfies the requirement.
        ****Note:
        If it does not satisfy, please assume a higher value of assumed_FTG_thickness_in, and re-run the whole class with the new value of assumed_FTG_thickness_in"""
        if self.shear_Vu_()<self.shear_strength_phiVc():
            return ("The assumed thickness of footing is satisfactory for shear, no revisions are necessary with respect to footing weight")
        else:
            return ('Please stop and re-run the class Structural_footing and enter another assumed_footing_thickness that is greater than the inital assumption.')


    def momentCS(self):
        """This function calculates the critical section of moment for calculating moment later on. This depends on the type of wall given by the problem, either concrete or masonry"""
        if self.wall_type=='masonry':
            return 0.5*(self.use_FTG_width()-self.wall_width_ft)+0.25*(self.wall_width_ft)
        elif self.wall_type=='concrete':
            return 0.5*(self.use_FTG_width()-self.wall_width_ft)-(self.assumed_effective_depth())/12
        else:
            return None


    def moment_Mu(self):
        """ This function calculates the moment based on the factored soil pressure calculated previously
        and the critical section of the moment"""
        return 0.5*self.factoredSoilPress_ksf()*self.momentCS()**2


    def reqKbar(self):
        """This function calculates the required Kbar based on the moment calculated previously and the assumed effective depth"""
        return (self.moment_Mu()*12)/(0.9*12*self.assumed_effective_depth()**2)


    def rho(self):
        """This function help user find rho by using the required kbar value calculated previously to find the appropriate value of rho in the table."""
        listofrho=[]
        for kbar,rho_Options in dict(self.table_of_reference()).items():
            if kbar>=self.reqKbar():
                listofrho.append(rho_Options)
        return np.min(listofrho)


    def reqA_s(self):
        """This function calculates the required area of steel by using the found rho value, wall width, and assumed effective depth"""
        return self.rho()*(self.wall_width_ft*12)*self.assumed_effective_depth()


    def As_min(self):
        """This function calculates the minimum area of steel required by ACI by using the value of fy and find the corresponding rho, and also using the wall width and assumed effective depth"""
        return TableA5[self.f_y,self.f_c_psi]*(self.wall_width_ft*12)*self.assumed_effective_depth()


    def reqA_s_Slabs_grade60Steel(self):
        """This function calculates the absolute minimum area of steel required by ACI using the wall width and assumed footing thickness"""
        return 0.0018*(self.wall_width_ft*12)*self.assumed_FTG_thickness_in


    def Controlling_As(self):
        """This function calculates the controlling area of steel, which is the larger of the three calculated areas"""
        return np.max([self.reqA_s(),self.As_min(),self.reqA_s_Slabs_grade60Steel()])


    def AS_available(self):
        """This function helps find the available options of bars and spacing baased on the controlling area and areas provided by the table"""
        listofAS=[]
        for barNum_spacing, area_steel in TableA4.items():
            if area_steel>=self.Controlling_As():
                listofAS.append(barNum_spacing)
        return listofAS


    def design(self):
        """This function allow user to design for reinforcing the steel by using the previous list of available options for areas of steel and letting user inputting what he choose from the list"""
        print("You can choose any tuple in the listofAs given by function AS_available(), where (Bar number, Bar spacing) and that will be what you use for reinforcement.")
        print("Bar number (first number of tuple):")
        bar_number=int(input())
        print("Bar spacing(second number of tuple):")
        bar_spacing=int(input())
        As_provided=TableA4[(bar_number,bar_spacing)]
        return print("Use No.",bar_number," at " ,bar_spacing, "in.oc. (As = ",As_provided,"in^2).")

    def l_available(self):
        """ This function calculates length available"""
        return (self.momentCS()*12)-3

    def development_length_checker(self):
        """This function calculates and check the adequacy of the development length based on the chosen design of steel reinforcement."""
        print("Please re-enter your chosen bar number from design() for the design for calculating the development length:")
        bar_number=int(input())
        print("Please re-enter your chosen bar spacing from design() for the design for calculating the development length:")
        bar_spacing=int(input())
        As_provided=TableA4[(bar_number,bar_spacing)]
    #reinforcement_location_t=1 (ACI assumption)
    #coating_e=1    (ACI assumption)
        if 3<=bar_number<=6:
            reinforcement_size_s=0.8
        elif 7<=bar_number<=11:
            reinforcement_size_s=1
        else:
            print("please enter a bar number within the range")
        numerator=1*1*reinforcement_size_s
        lambda_value=1          #normal-weight concrete
        K_tr=0                  #permitted by ACI Code (conservative)
        K_ER=self.Controlling_As()/As_provided
        d_b=TableA1[bar_number][0]
        c_b=np.min([(3+0.5*d_b), (0.5*bar_spacing)]) #the smaller of either the distance from the center of the bar to the nearest concrete surface or one-half the center to center spacing of the bars being developed

        if ((c_b+K_tr)/d_b) >2.5:
            denominator=2.5
        else:
            denominator=(c_b+K_tr)/d_b
        K_D=Table5_1[(self.f_y,self.f_c_psi)]
        development_length=(K_D/lambda_value)*(numerator/denominator)*K_ER*d_b
        if development_length<=self.l_available():
          return development_length,("The development length provided is adequate.")
        else:
          return development_length,("The development length provided is not adequate.")

    def longitudinal_steel(self):
        """ This function calculate the area for longitudinal steel for considering the shrink and temperature requirement by ACI"""
        return 0.0018*self.req_FTG_width() *12*self.assumed_FTG_thickness_in


    def AS_longitudinal_available(self):
        """ This function provides user the available list of areas for longitudinal steel and user can choose any tuple from this list for designing longitudinal steel"""
        listofAS_longitudinal_steel=[]
        for barNum_numofbar, area_provided in TableA2.items():
            if area_provided>=self.longitudinal_steel():
                listofAS_longitudinal_steel.append(barNum_numofbar)
        return listofAS_longitudinal_steel


    def design_longitudinal(self):
        """ This function allow user to input the design they want for longitudinal steel by inputing their choice after looking at the list of available options from the previous function"""
    #To design, user can choose any of the options in the listofAs_longitudinal_steel, which contains areas of steel that satifies the area requirement
        print("You can choose any tuple in the listofAs_longitudinal from AS_longitudinal_available(), where (Bar number, Number of bars) and that will be what you use for reinforcement.")
        print("Bar number (first number of tuple):")
        bar_num_longitudinal=int(input())
        print("Number of bars (second number of tuple):")
        num_bars=int(input())
        As_longitudinal_provided=TableA2[(bar_num_longitudinal,num_bars)]
        return print("Use ",num_bars," No. ", bar_num_longitudinal, " bars (As = ",As_longitudinal_provided,"in^2) spaced equally")
