import 'package:flutter/material.dart';

class Stats extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          width: 1124,
          height: 747,
          clipBehavior: Clip.antiAlias,
          decoration: BoxDecoration(color: Colors.white),
          child: Stack(
            children: [
              Positioned(
                left: 0,
                top: 0,
                child: Container(
                  width: 1124,
                  height: 747,
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment(0.00, -1.00),
                      end: Alignment(0, 1),
                      colors: [Color(0xFF0D0802), Color(0xFF4B8791)],
                    ),
                  ),
                ),
              ),
              Positioned(
                left: 224,
                top: 37,
                child: Container(
                  width: 871,
                  height: 658,
                  child: Stack(
                    children: [
                      Positioned(
                        left: 0,
                        top: 0,
                        child: Container(
                          width: 871,
                          height: 186,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 608,
                                top: 0,
                                child: Container(
                                  width: 263,
                                  height: 183,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 263,
                                          height: 36,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF4B8791),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 263,
                                          height: 37,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'B',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 30,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'S',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 62,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'G',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 99,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'P',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 140,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'D',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 181,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'M',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 222,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'G',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ],
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 0,
                                        top: 46,
                                        child: Container(
                                          width: 263,
                                          height: 137,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 263,
                                                  height: 137,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 26,
                                                top: 17,
                                                child: SizedBox(
                                                  width: 212,
                                                  height: 40,
                                                  child: Text(
                                                    'PvP',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 29,
                                                top: 76,
                                                child: SizedBox(
                                                  width: 206,
                                                  height: 60,
                                                  child: Text(
                                                    '46%',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ],
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 295,
                                top: 2,
                                child: Container(
                                  width: 263,
                                  height: 183,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 263,
                                          height: 36,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF4B8791),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 263,
                                          height: 37,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'B',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 30,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'S',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 62,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'G',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 99,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'P',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 140,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'D',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 181,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'M',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 222,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'G',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ],
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 0,
                                        top: 46,
                                        child: Container(
                                          width: 263,
                                          height: 137,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 263,
                                                  height: 137,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 26,
                                                top: 17,
                                                child: SizedBox(
                                                  width: 212,
                                                  height: 40,
                                                  child: Text(
                                                    'PvT',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 29,
                                                top: 76,
                                                child: SizedBox(
                                                  width: 206,
                                                  height: 60,
                                                  child: Text(
                                                    '46%',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ],
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 0,
                                top: 3,
                                child: Container(
                                  width: 263,
                                  height: 183,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 263,
                                          height: 36,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF4B8791),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 263,
                                          height: 37,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'B',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 30,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'S',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 62,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'G',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 99,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'P',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 140,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'D',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 181,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'M',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 222,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 41,
                                                  height: 36,
                                                  child: Text(
                                                    'G',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ],
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 0,
                                        top: 46,
                                        child: Container(
                                          width: 263,
                                          height: 137,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 263,
                                                  height: 137,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 26,
                                                top: 17,
                                                child: SizedBox(
                                                  width: 212,
                                                  height: 40,
                                                  child: Text(
                                                    'PvZ',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 29,
                                                top: 76,
                                                child: SizedBox(
                                                  width: 206,
                                                  height: 60,
                                                  child: Text(
                                                    '46%',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 30,
                                                      fontFamily: 'Inter',
                                                      fontWeight: FontWeight.w400,
                                                      height: 0,
                                                    ),
                                                  ),
                                                ),
                                              ),
                                            ],
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      Positioned(
                        left: 3,
                        top: 217,
                        child: Container(
                          width: 863,
                          height: 441,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 863,
                                  height: 55.37,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 863,
                                          height: 55.37,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF4B8791),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: SizedBox(
                                          width: 191.44,
                                          height: 55.37,
                                          child: Text(
                                            'Race',
                                            textAlign: TextAlign.center,
                                            style: TextStyle(
                                              color: Colors.white,
                                              fontSize: 30,
                                              fontFamily: 'Inter',
                                              fontWeight: FontWeight.w400,
                                              height: 0,
                                            ),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 217.50,
                                        top: 0,
                                        child: SizedBox(
                                          width: 165.38,
                                          height: 55.37,
                                          child: Text(
                                            'Rank',
                                            textAlign: TextAlign.center,
                                            style: TextStyle(
                                              color: Colors.white,
                                              fontSize: 30,
                                              fontFamily: 'Inter',
                                              fontWeight: FontWeight.w400,
                                              height: 0,
                                            ),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 396.92,
                                        top: 0,
                                        child: SizedBox(
                                          width: 165.38,
                                          height: 55.37,
                                          child: Text(
                                            'Match Up',
                                            textAlign: TextAlign.center,
                                            style: TextStyle(
                                              color: Colors.white,
                                              fontSize: 30,
                                              fontFamily: 'Inter',
                                              fontWeight: FontWeight.w400,
                                              height: 0,
                                            ),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 591.37,
                                        top: 0,
                                        child: SizedBox(
                                          width: 194.45,
                                          height: 55.37,
                                          child: Text(
                                            'Order By',
                                            textAlign: TextAlign.center,
                                            style: TextStyle(
                                              color: Colors.white,
                                              fontSize: 30,
                                              fontFamily: 'Inter',
                                              fontWeight: FontWeight.w400,
                                              height: 0,
                                            ),
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 0,
                                top: 65.26,
                                child: Container(
                                  width: 863,
                                  height: 375.74,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 863,
                                          height: 375.74,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF34585E),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 14.03,
                                        top: 11.87,
                                        child: Container(
                                          width: 838.94,
                                          height: 344.10,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 838.94,
                                                  height: 51.42,
                                                  child: Stack(
                                                    children: [
                                                      Positioned(
                                                        left: 0,
                                                        top: 0,
                                                        child: Container(
                                                          width: 834.93,
                                                          height: 51.42,
                                                          decoration: ShapeDecoration(
                                                            color: Color(0xFF2B4547),
                                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 1,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Build Name',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 161.37,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Rank',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 339.79,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Match Ups',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 526.22,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Strongest Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 670.55,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Weakest   Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                    ],
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 73.17,
                                                child: Container(
                                                  width: 838.94,
                                                  height: 51.42,
                                                  child: Stack(
                                                    children: [
                                                      Positioned(
                                                        left: 0,
                                                        top: 0,
                                                        child: Container(
                                                          width: 834.93,
                                                          height: 51.42,
                                                          decoration: ShapeDecoration(
                                                            color: Color(0xFF2B4547),
                                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 1,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Build Name',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 161.37,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Rank',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 339.79,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Match Ups',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 526.22,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Strongest Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 670.55,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Weakest   Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                    ],
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 146.34,
                                                child: Container(
                                                  width: 838.94,
                                                  height: 51.42,
                                                  child: Stack(
                                                    children: [
                                                      Positioned(
                                                        left: 0,
                                                        top: 0,
                                                        child: Container(
                                                          width: 834.93,
                                                          height: 51.42,
                                                          decoration: ShapeDecoration(
                                                            color: Color(0xFF2B4547),
                                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 1,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Build Name',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 161.37,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Rank',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 339.79,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Match Ups',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 526.22,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Strongest Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 670.55,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Weakest   Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                    ],
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 219.51,
                                                child: Container(
                                                  width: 838.94,
                                                  height: 51.42,
                                                  child: Stack(
                                                    children: [
                                                      Positioned(
                                                        left: 0,
                                                        top: 0,
                                                        child: Container(
                                                          width: 834.93,
                                                          height: 51.42,
                                                          decoration: ShapeDecoration(
                                                            color: Color(0xFF2B4547),
                                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 1,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Build Name',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 161.37,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Rank',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 339.79,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Match Ups',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 526.22,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Strongest Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 670.55,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Weakest   Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                    ],
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 292.68,
                                                child: Container(
                                                  width: 838.94,
                                                  height: 51.42,
                                                  child: Stack(
                                                    children: [
                                                      Positioned(
                                                        left: 0,
                                                        top: 0,
                                                        child: Container(
                                                          width: 834.93,
                                                          height: 51.42,
                                                          decoration: ShapeDecoration(
                                                            color: Color(0xFF2B4547),
                                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 1,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Build Name',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 161.37,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Rank',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 339.79,
                                                        top: 13.84,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Match Ups',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 526.22,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Strongest Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                      Positioned(
                                                        left: 670.55,
                                                        top: 1.98,
                                                        child: SizedBox(
                                                          width: 168.39,
                                                          height: 23.73,
                                                          child: Text(
                                                            'Weakest   Against',
                                                            textAlign: TextAlign.center,
                                                            style: TextStyle(
                                                              color: Colors.white,
                                                              fontSize: 20,
                                                              fontFamily: 'Inter',
                                                              fontWeight: FontWeight.w400,
                                                              height: 0,
                                                            ),
                                                          ),
                                                        ),
                                                      ),
                                                    ],
                                                  ),
                                                ),
                                              ),
                                            ],
                                          ),
                                        ),
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              Positioned(
                left: 0,
                top: 0,
                child: Container(
                  width: 149,
                  height: 747,
                  child: Stack(
                    children: [
                      Positioned(
                        left: 0,
                        top: 0,
                        child: Container(
                          width: 149,
                          height: 747,
                          decoration: BoxDecoration(color: Color(0xFF3D6A71)),
                        ),
                      ),
                      Positioned(
                        left: 14.67,
                        top: 22,
                        child: Container(
                          width: 111.75,
                          height: 37.72,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 111.75,
                                  height: 37.72,
                                  decoration: ShapeDecoration(
                                    color: Color(0xFF34585E),
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 11.29,
                                top: 8.38,
                                child: SizedBox(
                                  width: 90.30,
                                  height: 17.81,
                                  child: Text(
                                    'Home',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 12,
                                      fontFamily: 'Inter',
                                      fontWeight: FontWeight.w400,
                                      height: 0,
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      Positioned(
                        left: 14.67,
                        top: 101.63,
                        child: Container(
                          width: 111.75,
                          height: 37.72,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 111.75,
                                  height: 37.72,
                                  decoration: ShapeDecoration(
                                    color: Color(0xFF34585E),
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 11.29,
                                top: 8.38,
                                child: SizedBox(
                                  width: 90.30,
                                  height: 17.81,
                                  child: Text(
                                    'Settings',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 12,
                                      fontFamily: 'Inter',
                                      fontWeight: FontWeight.w400,
                                      height: 0,
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      Positioned(
                        left: 14.67,
                        top: 185.44,
                        child: Container(
                          width: 111.75,
                          height: 37.72,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 111.75,
                                  height: 37.72,
                                  decoration: ShapeDecoration(
                                    color: Color(0xFF34585E),
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 11.29,
                                top: 8.38,
                                child: SizedBox(
                                  width: 90.30,
                                  height: 17.81,
                                  child: Text(
                                    'Builds',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 12,
                                      fontFamily: 'Inter',
                                      fontWeight: FontWeight.w400,
                                      height: 0,
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      Positioned(
                        left: 14.67,
                        top: 274.49,
                        child: Container(
                          width: 111.75,
                          height: 37.72,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 111.75,
                                  height: 37.72,
                                  decoration: ShapeDecoration(
                                    color: Color(0xFF34585E),
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 11.29,
                                top: 8.38,
                                child: SizedBox(
                                  width: 90.30,
                                  height: 17.81,
                                  child: Text(
                                    'Stats',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 12,
                                      fontFamily: 'Inter',
                                      fontWeight: FontWeight.w400,
                                      height: 0,
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}
