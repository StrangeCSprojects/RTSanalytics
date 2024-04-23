import 'package:flutter/material.dart';
import 'stats.dart';
import 'dart:io'; 

void main() {
  startup();
  runApp(const MainContent());
}

void startup() async {
  // Command to execute
  String command = 'py';
  // Arguments to pass to the command
  List<String> arguments = ['-m', 'server_tools.sc2.sc2_server_api'];

  try {
    // Running the process
    ProcessResult results = await Process.run(
      command, 
      arguments,
      workingDirectory: '.',
      );

    // Outputting the results
    print('The process exited with code ${results.exitCode}');
    print('Output:\n${results.stdout}');
    print('Errors (if any):\n${results.stderr}');
  } catch (e) {
    print('An error occurred: $e');
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
