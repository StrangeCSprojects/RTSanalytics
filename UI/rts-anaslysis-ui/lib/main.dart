import 'package:flutter/material.dart';
import 'stats.dart';
import 'dart:io'; 

void main() {
  startup();
  runApp(const MainContent());
}

void startup() async {
  String workingDirectory = '.';
  String pythonExecutable = '$workingDirectory\\python\\python.exe';
  List<String> runArg = ['-m', 'server_tools.sc2.sc2_server_api'];
  List<String> installArg = ['-m', 'pip', 'install', '-r', 'requirements.txt'];


  try {
    // ProcessResult install = await Process.run(
    //   pythonExecutable, 
    //   installArg,
    //   workingDirectory: '.',
    // );
    ProcessResult run = await Process.run(
      pythonExecutable, 
      runArg,
      workingDirectory: '.',
    );
  } catch (e) {
    print('Error starting server: $e');
  }
}

class MainContent extends StatelessWidget {
  const MainContent({super.key});

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