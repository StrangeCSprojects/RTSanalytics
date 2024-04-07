import 'dart:html';

import 'package:flutter/material.dart';
import 'home.dart';


void main() {
  runApp(const FigmaToCodeApp());
}

class FigmaToCodeApp extends StatelessWidget {
  const FigmaToCodeApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
              body: Stack(
                children: [
                  Positioned.fill(
                    child: Home(),
                  ),
            ],
          ),
        ),
    );
  }
}
