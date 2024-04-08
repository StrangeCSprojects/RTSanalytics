import 'package:flutter/material.dart';

class Settings extends StatelessWidget {
  const Settings({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          width: 1124,
          height: 747,
          clipBehavior: Clip.antiAlias,
          decoration: const BoxDecoration(color: Colors.white),
          child: Stack(
            children: [
              Positioned(
                left: 0,
                top: 0,
                child: Container(
                  width: 1124,
                  height: 747,
                  decoration: const BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment(0.00, -1.00),
                      end: Alignment(0, 1),
                      colors: [Color(0xFF0D0802), Color(0xFF4B8791)],
                    ),
                  ),
                ),
              ),
              Positioned(
                left: 243,
                top: 99,
                child: SizedBox(
                  width: 781,
                  height: 549,
                  child: Stack(
                    children: [
                      Positioned(
                        left: 0,
                        top: 0,
                        child: Container(
                          width: 781,
                          height: 549,
                          decoration: const BoxDecoration(color: Color(0xFF3D6A71)),
                        ),
                      ),
                      Positioned(
                        left: 55,
                        top: 210,
                        child: SizedBox(
                          width: 671,
                          height: 129,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 671,
                                  height: 129,
                                  decoration: const BoxDecoration(color: Color(0xFF2C4749)),
                                ),
                              ),
                              const Positioned(
                                left: 18,
                                top: 52,
                                child: SizedBox(
                                  width: 129,
                                  child: Text(
                                    'Email:',
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
                                left: 147,
                                top: 53,
                                child: SizedBox(
                                  width: 356,
                                  child: Text(
                                    'JohnSmith@gmail.com',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      color: Colors.white.withOpacity(0.5),
                                      fontSize: 20,
                                      fontFamily: 'Inter',
                                      fontWeight: FontWeight.w400,
                                      height: 0,
                                    ),
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 508,
                                top: 39,
                                child: SizedBox(
                                  width: 145,
                                  height: 50,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 145,
                                          height: 50,
                                          decoration: ShapeDecoration(
                                            color: const Color(0xFF3AA4B5),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      const Positioned(
                                        left: 0,
                                        top: 12.50,
                                        child: SizedBox(
                                          width: 145,
                                          height: 26.79,
                                          child: Text(
                                            'Change Email',
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
                      Positioned(
                        left: 55,
                        top: 377,
                        child: SizedBox(
                          width: 671,
                          height: 129,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 671,
                                  height: 129,
                                  decoration: const BoxDecoration(color: Color(0xFF2C4749)),
                                ),
                              ),
                              const Positioned(
                                left: 18,
                                top: 52,
                                child: SizedBox(
                                  width: 129,
                                  child: Text(
                                    'Password:',
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
                                left: 147,
                                top: 53,
                                child: SizedBox(
                                  width: 356,
                                  child: Text(
                                    '********',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      color: Colors.white.withOpacity(0.5),
                                      fontSize: 20,
                                      fontFamily: 'Inter',
                                      fontWeight: FontWeight.w400,
                                      height: 0,
                                    ),
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 508,
                                top: 39,
                                child: SizedBox(
                                  width: 145,
                                  height: 50,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 145,
                                          height: 50,
                                          decoration: ShapeDecoration(
                                            color: const Color(0xFF3AA4B5),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      const Positioned(
                                        left: 0,
                                        top: 12.50,
                                        child: SizedBox(
                                          width: 145,
                                          height: 26.79,
                                          child: Text(
                                            'Change Password',
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
                      Positioned(
                        left: 55,
                        top: 43,
                        child: SizedBox(
                          width: 671,
                          height: 129,
                          child: Stack(
                            children: [
                              Positioned(
                                left: 0,
                                top: 0,
                                child: Container(
                                  width: 671,
                                  height: 129,
                                  decoration: const BoxDecoration(color: Color(0xFF2C4749)),
                                ),
                              ),
                              const Positioned(
                                left: 18,
                                top: 52,
                                child: SizedBox(
                                  width: 129,
                                  child: Text(
                                    'Name:',
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
                                left: 147,
                                top: 53,
                                child: SizedBox(
                                  width: 356,
                                  child: Text(
                                    'John Smith',
                                    textAlign: TextAlign.center,
                                    style: TextStyle(
                                      color: Colors.white.withOpacity(0.5),
                                      fontSize: 20,
                                      fontFamily: 'Inter',
                                      fontWeight: FontWeight.w400,
                                      height: 0,
                                    ),
                                  ),
                                ),
                              ),
                              Positioned(
                                left: 508,
                                top: 39,
                                child: SizedBox(
                                  width: 145,
                                  height: 50,
                                  child: Stack(
                                    children: [
                                      Positioned(
                                        left: 0,
                                        top: 0,
                                        child: Container(
                                          width: 145,
                                          height: 50,
                                          decoration: ShapeDecoration(
                                            color: const Color(0xFF3AA4B5),
                                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                          ),
                                        ),
                                      ),
                                      const Positioned(
                                        left: 0,
                                        top: 12.50,
                                        child: SizedBox(
                                          width: 145,
                                          height: 26.79,
                                          child: Text(
                                            'Change Name',
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
              Positioned(
                left: 0,
                top: 0,
                child: SizedBox(
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
                          decoration: const BoxDecoration(color: Color(0xFF3D6A71)),
                        ),
                      ),
                      Positioned(
                        left: 14.67,
                        top: 22,
                        child: SizedBox(
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
                                    color: const Color(0xFF34585E),
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                  ),
                                ),
                              ),
                              const Positioned(
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
                        child: SizedBox(
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
                                    color: const Color(0xFF34585E),
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                  ),
                                ),
                              ),
                              const Positioned(
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
                        child: SizedBox(
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
                                    color: const Color(0xFF34585E),
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                  ),
                                ),
                              ),
                              const Positioned(
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
                        child: SizedBox(
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
                                    color: const Color(0xFF34585E),
                                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
                                  ),
                                ),
                              ),
                              const Positioned(
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