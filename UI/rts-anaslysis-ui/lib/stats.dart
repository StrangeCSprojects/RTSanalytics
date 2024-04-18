import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'globals.dart';
import 'dart:html' as html;

void downloadFile(String url, String fileName) {
  // Create an anchor element
  final anchor = html.AnchorElement(href: url)
    ..setAttribute("download", fileName)
    ..click();
}

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
        BuildOrderContainer(),
        SizedBox(height: 36),
      ],
    );
  }
}

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
      child: RaceWinRate(),
    );
  }
}

class RaceWinRate extends StatelessWidget {
  const RaceWinRate({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 871,
      height: 126.75,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: const [
          RaceRateFormat(title: 'Protoss', percentage: '46%'),
          RaceRateFormat(title: 'Terran', percentage: '46%'),
          RaceRateFormat(title: 'Zerg', percentage: '46%'),
        ],
      ),
    );
  }
}


class RaceRateFormat extends StatelessWidget {
  final String title;
  final String percentage;

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
          Text(percentage, style: const TextStyle(color: Colors.white, fontSize: 30)),
        ],
      ),
    );
  }
}

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

class BuildOrderContainer extends StatelessWidget {
  const BuildOrderContainer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
  return Container(
    width: 868,
    height: 347.88,
    decoration: ShapeDecoration(
      color: Color(0xFF34585E),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
    ),
    child: ListView(
    shrinkWrap: true,
    children: const [
      BuildOrderWidget(name: 'Build Name', race: 'Race', winRate: 'Win rate'),
      BuildOrderWidget(name: 'organic', race: 'Terran', winRate: '98%', buildorder: "something terrrable has happened",),
      BuildOrderWidget(name: 'organic', race: 'Terran', winRate: '98%', buildorder: "something terrrable has happened",),
      BuildOrderWidget(name: 'organic', race: 'Terran', winRate: '98%', buildorder: "something terrrable has happened",),
      BuildOrderWidget(name: 'organic', race: 'Terran', winRate: '98%', buildorder: "something terrrable has happened",),
      BuildOrderWidget(name: 'organic', race: 'Terran', winRate: '98%', buildorder: "something terrrable has happened",),
      BuildOrderWidget(name: 'organic', race: 'Terran', winRate: '98%', buildorder: "something terrrable has happened",),
      BuildOrderWidget(name: 'organic', race: 'Terran', winRate: '98%', buildorder: "something terrrable has happened",),
      BuildOrderSideSpacer(),
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

class BuildOrderWidget extends StatelessWidget {
  final String name;
  final String race;
  final String winRate;
  final String buildorder;  //placeholder for build order

  const BuildOrderWidget({
    Key? key,
    required this.name,
    required this.race,
    required this.winRate,
    this.buildorder = 'No Buildorder found',
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(children: [Container(
          width: 868,
          height: 25,
        )],),
        Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [ 
            BuildOrderSideSpacer(),
            Container(
              width: 838,
              height: 48,
              decoration: ShapeDecoration(
                color: Color(0xFF2B4547),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(5)),
              ),
              child: Row(
                children: [
                  BuildOrderSideSpacer(),
                  Expanded(child: Text(name,textAlign: TextAlign.center, style: const TextStyle(color: Colors.white, fontSize: 30))),
                  Expanded(child: Text(race, textAlign: TextAlign.center,style: const TextStyle(color: Colors.white, fontSize: 30))),
                  Expanded(child: Text(winRate,textAlign: TextAlign.center, style: const TextStyle(color: Colors.white, fontSize: 30))),
                  Expanded( // Keep the Expanded widget
                  child: Center( // Center the button
                    child: SizedBox(
                      width: 200,
                      height: 60,
                      child: ElevatedButton(
                        onPressed: kIsWeb ? null : () {
                          String downloadurl = './downloads/rtsanalytics.exe';
                          String fileName = 'downloadedFile.pdf';
                          downloadFile(downloadurl, fileName);
                        },
                        child: Text('Display', style: TextStyle(color: Colors.white, fontSize: 30)),
                        style: ElevatedButton.styleFrom(
                          backgroundColor: kIsWeb ? Colors.grey : Color(0xFF34585E), // background color
                          surfaceTintColor: Colors.grey,
                        ),
                      ),
                    )
                  ),
                ),
                  BuildOrderSideSpacer(),
                ],
              ),
            ),
            BuildOrderSideSpacer(),
          ],
        ),
      ],
    ); 
  }
}