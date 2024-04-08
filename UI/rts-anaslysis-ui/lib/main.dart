import 'dart:html';

import 'package:flutter/material.dart';
import 'stats.dart';


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
            Positioned.fill(child: DecoratedBox(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment(0.00, -1.00),
                  end: Alignment(0, 1),
                  colors: [Color(0xFF0D0802), Color(0xFF4B8791)],
                ),
              ),
            ),
            ),
            Positioned.fill(
              child: Stats(),
            ),
          ],
        ),
      ),
    );
  }
}
