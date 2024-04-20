import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'globals.dart';
import 'dart:html' as html;
import 'dart:convert';
import 'package:http/http.dart' as http;

const Color backgroundColor = Color.fromARGB(0, 255, 255, 255);

class Stats extends StatelessWidget {
  const Stats({super.key});

  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: backgroundColor
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        children: const [
          ContentBox(),
        ],
      ),
    );
  }
}

class ContentBox extends StatelessWidget {
  const ContentBox({Key? key}) : super(key: key);

  Widget build(BuildContext context) {
    return Column(
      children: [
        RaceRateContents(),
        SizedBox(height: 36),
        ContentTitle(),
        SizedBox(height: 36),
        BuildOrderContents(),
        SizedBox(height: 36),
      ],
    );
  }
}

// Race winrates
class RaceRateContents extends StatelessWidget {
  const RaceRateContents({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 871,
      height: 180,
      color:  Color.fromARGB(0, 75, 135, 145),
      child: WinRatesWidget(),
    );
  }
}

class RaceRateFormat extends StatelessWidget {
  final String title;
  final double percentage;

  const RaceRateFormat({Key? key, required this.title, required this.percentage}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 263,
      height: 126.75,
      decoration: BoxDecoration(
        color: const Color(0xFF34585E),
        borderRadius: BorderRadius.circular(5),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(title, style: const TextStyle(color: Colors.white, fontSize: 30)),
          const SizedBox(height: 15),
          Text('${percentage.toStringAsFixed(0)}%', style: const TextStyle(color: Colors.white, fontSize: 30)),
        ],
      ),
    );
  }
}

class WinRatesWidget extends StatefulWidget {
  @override
  _WinRatesWidgetState createState() => _WinRatesWidgetState();
}

class _WinRatesWidgetState extends State<WinRatesWidget> {
  double protoss = 0.0;
  double terran = 0.0;
  double zerg = 0.0;

  @override
  void initState() {
    super.initState();
    fetchPercentage();
  }

  Future<void> fetchPercentage() async {
    try {
      final response = await http.get(Uri.parse('http://127.0.0.1:5010/get_winrates_race'));
      if (response.statusCode == 200) {
        var jsonResponse = jsonDecode(response.body);
        setState(() {
          protoss = jsonResponse['protoss'];
          terran = jsonResponse['terran'];
          zerg = jsonResponse['zerg'];
        });
      } else {
        throw Exception('Failed to load percentage');
      }
    } catch (e) {
      print('Error occurred: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 871,
      height: 126.75,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          RaceRateFormat(title: 'Protoss', percentage: protoss),
          RaceRateFormat(title: 'Terran', percentage: terran),
          RaceRateFormat(title: 'Zerg', percentage: zerg),
        ],
      ),
    );
  }
}

// Builds list
class ContentTitle extends StatelessWidget {
  final ContentTitles = ['Build Order', 'Race', 'Win rate'];

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 868,
      height: 71.24,
      decoration: BoxDecoration(
        color: const Color(0xFF4B8791),
        borderRadius: BorderRadius.circular(5),
      ),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 15),
        width: 838,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: ContentTitles
              .map((stat) => Expanded( // Wrap Text widget with Expanded
                    child: Text(
                      stat,
                      textAlign: TextAlign.center,
                      style: const TextStyle(color: Colors.white, fontSize: 30),
                    ),
                  ))
              .toList() +
              [
                Expanded( // Keep the Expanded widget
                  child: Center( // Center the button
                    child: SizedBox( // Use SizedBox to set the width and height of the button
                      width: 200, // Set the width of the button
                      height: 60, // Set the height of the button
                      child: ElevatedButton(
                        onPressed: kIsWeb ? () {
                          // Handle button press here for web
                        } : null,
                        child: Tooltip(
                          message: kIsWeb ? '' : 'currently not able to import user submitted replys',
                          child: Text(kIsWeb ? 'Download' : 'Import', style: TextStyle(color: Colors.white, fontSize: 30)),
                        ),
                        style: ButtonStyle(
                          backgroundColor: MaterialStateProperty.resolveWith<Color>(
                            (Set<MaterialState> states) {
                              if (states.contains(MaterialState.pressed))
                                return kIsWeb ? Color(0xFF34585E) : Color.fromARGB(255, 68, 68, 68);
                              return kIsWeb ? Color(0xFF34585E) : Color.fromARGB(255, 68, 68, 68);
                            },
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
              ]
          ),
      ),
    );
  } 
}

class BuildOrderContents extends StatelessWidget {
  const BuildOrderContents({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 868,
      height: 347.88,
      color: Color.fromARGB(76, 2, 3, 3),
      child: BuildOrderWidget(),
    );
  }
  
}

class BuildOrderContainer extends StatelessWidget {
  final String name;
  final String race;
  final String winrate;


  const BuildOrderContainer({Key? key, required this.name, required this.race, required this.winrate}) : super(key: key);

  @override
  Widget build(BuildContext context) {
  return Container(
    height: 50,
    decoration: ShapeDecoration(
      color: Color(0xFF34585E),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
    ),
    child: Row(
    children: [

        Text('$name $race $winrate', style: const TextStyle(color: Colors.white, fontSize: 30)),
        
    ],
      ),
    );
  }
}

class BuildOrderSideSpacer extends StatelessWidget {
  const BuildOrderSideSpacer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 15,
      height: 48,
      decoration: ShapeDecoration(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
      )
    );
  }
}

void downloadFile(String url, String fileName) {
  // Create an anchor element
  final anchor = html.AnchorElement(href: url)
    ..setAttribute("download", fileName)
    ..click();
}



class BuildOrderWidget extends StatefulWidget {
  @override
  _BuildOrderWidgetState createState() =>  _BuildOrderWidgetState();
}

class _BuildOrderWidgetState extends State<BuildOrderWidget> {
  List<BuildOrderList> buildOrders = [];

  @override
  void initState()  {
    super.initState();
    fetchBuilds();
  }

  Future<void> fetchBuilds() async {
    try {
      final response = await http.get(Uri.parse('http://127.0.0.1:5010/get_build_orders'));
      if (response.statusCode == 200) {
        var jsonResponse = jsonDecode(response.body);
        List<BuildOrderList> tempBuilds = [];
        for (var build in jsonResponse) {
          tempBuilds.add(BuildOrderList(name: build['name'], race: build['race'], winrate: build['winrate'].toString()));
        }
        setState(() {
          buildOrders = tempBuilds;
        });
      } else {
        throw Exception('Failed to build information');
      }
    } catch (e) {
      print('Error occurred: $e');
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return ListView(
      children: buildOrders.map((build) => BuildOrderContainer(name: build.name, race: build.race, winrate: build.winrate)).toList(),
    );
  }



}

class BuildOrderList {
  final String name;
  final String race;
  final String winrate;

  BuildOrderList({
    required this.name,
    required this.race,
    required this.winrate,
  });
}