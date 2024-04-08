import 'package:flutter/material.dart';

class Builds extends StatelessWidget {
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
                left: 172,
                top: 43,
                child: Container(
                  width: 901,
                  height: 666,
                  child: Stack(
                    children: [
                      Positioned(
                        left: 0,
                        top: 146,
                        child: Container(
                          width: 901,
                          height: 520,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 370,
                                child: Container(
                                  width: 901,
                                  height: 150,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 5,
                                        top: 0,
                                        child: Container(
                                          width: 896,
                                          height: 150,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF2B4547),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 844,
                                        top: 49,
                                        child: Container(
                                          width: 48,
                                          height: 45,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 47,
                                                  height: 45,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 1,
                                                top: 15,
                                                child: SizedBox(
                                                  width: 47,
                                                  height: 11,
                                                  child: Text(
                                                    'Import',
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
                                        left: 16,
                                        top: 19,
                                        child: Container(
                                          width: 139,
                                          height: 22,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 1,
                                                top: 0,
                                                child: Container(
                                                  width: 138,
                                                  height: 22,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 2,
                                                child: SizedBox(
                                                  width: 134,
                                                  height: 16,
                                                  child: Text(
                                                    'Name',
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
                                        left: 178,
                                        top: 15,
                                        child: Container(
                                          width: 644,
                                          height: 119,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 644,
                                                  height: 119,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 97,
                                                top: 34,
                                                child: SizedBox(
                                                  width: 407,
                                                  height: 57,
                                                  child: Text(
                                                    'Build',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 40,
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
                                        left: 80,
                                        top: 85,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 0,
                                                child: Container(
                                                  width: 58,
                                                  height: 18,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Type',
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
                                        left: 0,
                                        top: 85,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 0,
                                                child: Container(
                                                  width: 58,
                                                  height: 18,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Race',
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
                                        left: 80,
                                        top: 54,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 1,
                                                child: Container(
                                                  width: 58,
                                                  height: 17,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Difficulty',
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
                                        left: 0,
                                        top: 54,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 1,
                                                child: Container(
                                                  width: 58,
                                                  height: 17,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Patch',
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
                              Positioned(
                                left: 0,
                                top: 185,
                                child: Container(
                                  width: 901,
                                  height: 150,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 5,
                                        top: 0,
                                        child: Container(
                                          width: 896,
                                          height: 150,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF2B4547),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 844,
                                        top: 49,
                                        child: Container(
                                          width: 48,
                                          height: 45,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 47,
                                                  height: 45,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 1,
                                                top: 15,
                                                child: SizedBox(
                                                  width: 47,
                                                  height: 11,
                                                  child: Text(
                                                    'Import',
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
                                        left: 16,
                                        top: 19,
                                        child: Container(
                                          width: 139,
                                          height: 22,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 1,
                                                top: 0,
                                                child: Container(
                                                  width: 138,
                                                  height: 22,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 2,
                                                child: SizedBox(
                                                  width: 134,
                                                  height: 16,
                                                  child: Text(
                                                    'Name',
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
                                        left: 178,
                                        top: 15,
                                        child: Container(
                                          width: 644,
                                          height: 119,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 644,
                                                  height: 119,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 97,
                                                top: 34,
                                                child: SizedBox(
                                                  width: 407,
                                                  height: 57,
                                                  child: Text(
                                                    'Build',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 40,
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
                                        left: 80,
                                        top: 85,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 0,
                                                child: Container(
                                                  width: 58,
                                                  height: 18,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Type',
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
                                        left: 0,
                                        top: 85,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 0,
                                                child: Container(
                                                  width: 58,
                                                  height: 18,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Race',
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
                                        left: 80,
                                        top: 54,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 1,
                                                child: Container(
                                                  width: 58,
                                                  height: 17,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Difficulty',
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
                                        left: 0,
                                        top: 54,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 1,
                                                child: Container(
                                                  width: 58,
                                                  height: 17,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Patch',
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
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 901,
                                  height: 150,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 5,
                                        top: 0,
                                        child: Container(
                                          width: 896,
                                          height: 150,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF2B4547),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 844,
                                        top: 49,
                                        child: Container(
                                          width: 48,
                                          height: 45,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 47,
                                                  height: 45,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 1,
                                                top: 15,
                                                child: SizedBox(
                                                  width: 47,
                                                  height: 11,
                                                  child: Text(
                                                    'Import',
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
                                        left: 16,
                                        top: 19,
                                        child: Container(
                                          width: 139,
                                          height: 22,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 1,
                                                top: 0,
                                                child: Container(
                                                  width: 138,
                                                  height: 22,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 2,
                                                child: SizedBox(
                                                  width: 134,
                                                  height: 16,
                                                  child: Text(
                                                    'Name',
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
                                        left: 178,
                                        top: 15,
                                        child: Container(
                                          width: 644,
                                          height: 119,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Container(
                                                  width: 644,
                                                  height: 119,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 97,
                                                top: 34,
                                                child: SizedBox(
                                                  width: 407,
                                                  height: 57,
                                                  child: Text(
                                                    'Build',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Colors.white,
                                                      fontSize: 40,
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
                                        left: 80,
                                        top: 85,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 0,
                                                child: Container(
                                                  width: 58,
                                                  height: 18,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Type',
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
                                        left: 0,
                                        top: 85,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 0,
                                                child: Container(
                                                  width: 58,
                                                  height: 18,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 1,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Race',
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
                                        left: 80,
                                        top: 54,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 1,
                                                child: Container(
                                                  width: 58,
                                                  height: 17,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Difficulty',
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
                                        left: 0,
                                        top: 54,
                                        child: Container(
                                          width: 92,
                                          height: 18,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 17,
                                                top: 1,
                                                child: Container(
                                                  width: 58,
                                                  height: 17,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 92,
                                                  height: 16,
                                                  child: Text(
                                                    'Patch',
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
                      ),
                      Positioned(
                        left: 7,
                        top: 0,
                        child: Container(
                          width: 725,
                          height: 89,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 1,
                                top: 47,
                                child: Container(
                                  width: 724,
                                  height: 42,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 724,
                                          height: 42,
                                          decoration: ShapeDecoration(
                                            color: Color(0xFF3D6A71),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      Positioned(
                                        left: 23,
                                        top: 9,
                                        child: Container(
                                          width: 91,
                                          height: 23,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 3,
                                                top: 0,
                                                child: Container(
                                                  width: 85,
                                                  height: 23,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(
                                                      borderRadius: BorderRadius.circular(15),
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 91,
                                                  height: 23,
                                                  child: Text(
                                                    'Search',
                                                    textAlign: TextAlign.center,
                                                    style: TextStyle(
                                                      color: Color(0xFFE1E0DF),
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
                                        left: 145,
                                        top: 9,
                                        child: Container(
                                          width: 91,
                                          height: 23,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 3,
                                                top: 0,
                                                child: Container(
                                                  width: 85,
                                                  height: 23,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(
                                                      borderRadius: BorderRadius.circular(15),
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 91,
                                                  height: 23,
                                                  child: Text(
                                                    'Race',
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
                                        left: 267,
                                        top: 9,
                                        child: Container(
                                          width: 91,
                                          height: 23,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 3,
                                                top: 0,
                                                child: Container(
                                                  width: 85,
                                                  height: 23,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(
                                                      borderRadius: BorderRadius.circular(15),
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 91,
                                                  height: 23,
                                                  child: Text(
                                                    'Difficulty',
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
                                        left: 511,
                                        top: 9,
                                        child: Container(
                                          width: 91,
                                          height: 23,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 3,
                                                top: 0,
                                                child: Container(
                                                  width: 85,
                                                  height: 23,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(
                                                      borderRadius: BorderRadius.circular(15),
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 91,
                                                  height: 23,
                                                  child: Text(
                                                    'Type',
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
                                        left: 389,
                                        top: 9,
                                        child: Container(
                                          width: 91,
                                          height: 23,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 3,
                                                top: 0,
                                                child: Container(
                                                  width: 85,
                                                  height: 23,
                                                  decoration: ShapeDecoration(
                                                    color: Color(0xFF34585E),
                                                    shape: RoundedRectangleBorder(
                                                      borderRadius: BorderRadius.circular(15),
                                                    ),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 91,
                                                  height: 23,
                                                  child: Text(
                                                    'Tier',
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
                                        left: 615,
                                        top: 14,
                                        child: Container(
                                          width: 100,
                                          height: 12,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 1,
                                                child: Container(
                                                  width: 11,
                                                  height: 11,
                                                  decoration: ShapeDecoration(
                                                    color: Colors.white,
                                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(2)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 19,
                                                top: 0,
                                                child: SizedBox(
                                                  width: 81,
                                                  height: 11,
                                                  child: Text(
                                                    'Current Patch',
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
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 655,
                                  height: 28,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 201,
                                        top: 1,
                                        child: Container(
                                          width: 133,
                                          height: 21,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Opacity(
                                                  opacity: 0,
                                                  child: Container(
                                                    width: 133,
                                                    height: 21,
                                                    decoration: BoxDecoration(color: Color(0xFFD9D9D9)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 1,
                                                top: 4,
                                                child: SizedBox(
                                                  width: 132,
                                                  height: 12,
                                                  child: Text(
                                                    'Community Builds\n',
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
                                        left: 472,
                                        top: 0,
                                        child: Container(
                                          width: 137,
                                          height: 21,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Opacity(
                                                  opacity: 0,
                                                  child: Container(
                                                    width: 133,
                                                    height: 21,
                                                    decoration: BoxDecoration(color: Color(0xFFD9D9D9)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 5,
                                                top: 3,
                                                child: SizedBox(
                                                  width: 132,
                                                  height: 12,
                                                  child: Text(
                                                    'Personal Builds\n',
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
                                        left: 6,
                                        top: 0,
                                        child: Container(
                                          width: 138,
                                          height: 21,
                                          child: Stack(
                                            children: [
                                              Positioned(
                                                left: 0,
                                                top: 0,
                                                child: Opacity(
                                                  opacity: 0,
                                                  child: Container(
                                                    width: 133,
                                                    height: 21,
                                                    decoration: BoxDecoration(color: Color(0xFFD9D9D9)),
                                                  ),
                                                ),
                                              ),
                                              Positioned(
                                                left: 6,
                                                top: 4,
                                                child: SizedBox(
                                                  width: 132,
                                                  height: 12,
                                                  child: Text(
                                                    'Meta Builds\n',
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
                                        left: 0,
                                        top: 26,
                                        child: Container(
                                          width: 655,
                                          height: 2,
                                          decoration: BoxDecoration(color: Colors.white),
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