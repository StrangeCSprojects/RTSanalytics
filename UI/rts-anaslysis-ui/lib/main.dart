
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'home.dart';
import 'stats.dart';


void main() {
  runApp(const FigmaToCodeApp());
}



class FigmaToCodeApp extends StatelessWidget {
  const FigmaToCodeApp({super.key});

  // // Fetch the output from the Python function
  // Future<String> fetchOutput() async {
  //   final response = await http.get(Uri.parse('http://localhost:5001//getPythonFunctionOutput'));
  //   if (response.statusCode == 200) {
  //     // If the server returns a 200 OK response, parse the JSON
  //     return jsonDecode(response.body)['data'];
  //   } else {
  //     // If the server did not return a 200 OK response,
  //     // throw an exception.
  //     throw Exception('Failed to load data');
  //   }
  // }

  // @override
  // Widget build(BuildContext context) {
  //   return MaterialApp(
  //     home: Scaffold(
  //       body: FutureBuilder<String>(
  //         future: fetchOutput(),
  //         builder: (context, snapshot) {
  //           if (snapshot.hasData) {
  //             return Text("Output from Python: ${snapshot.data}");
  //           } else if (snapshot.hasError) {
  //             return Text("${snapshot.error}");
  //           }
  //           // By default, show a loading spinner.
  //           return const CircularProgressIndicator();
  //         },
  //       ),
  //     ),
  //   );
  // }



  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
              body: Stack(
                children: [
                  Positioned.fill(
                    child: Stats(),
                  ),
            ],
          ),
        ),
    );
  }
}
