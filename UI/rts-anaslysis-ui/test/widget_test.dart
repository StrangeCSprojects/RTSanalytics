import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import '../lib/stats.dart';

void main() {
  testWidgets('Stats widget test', (WidgetTester tester) async {
    // Build the Stats widget and trigger a frame.
    await tester.pumpWidget(const Stats());

    // Verify that the Stats widget is displayed.
    expect(find.byType(Stats), findsOneWidget);

    // Verify that the HomeScreen widget is displayed.
    expect(find.byType(HomeScreen), findsOneWidget);

    // Verify that the ContentBox widget is displayed.
    expect(find.byType(ContentBox), findsOneWidget);

    // Verify that the RaceRateContents widget is displayed.
    expect(find.byType(RaceRateContents), findsOneWidget);

    // Verify that the RaceWinRate widget is displayed.
    expect(find.byType(RaceWinRate), findsOneWidget);

    // Verify that the RaceRateFormat widget is displayed.
    expect(find.byType(RaceRateFormat), findsWidgets);

    // Verify that the ContentTitle widget is displayed.
    expect(find.byType(ContentTitle), findsOneWidget);

    // Verify that the BuildOrderContainer widget is displayed.
    expect(find.byType(BuildOrderContainer), findsOneWidget);

    // Verify that the BuildOrderWidget widget is displayed.
    expect(find.byType(BuildOrderWidget), findsWidgets);
  });
}