import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  // ignore: library_private_types_in_public_api
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  bool showSignUp = false;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 1200,
      height: 800,
      decoration: const BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment(0.00, -1.00),
          end: Alignment(0, 1),
          colors: [Color(0xFF0D0802), Color(0xFF4B8791)],
        ),
      ),
      child: Scaffold(
        body: SingleChildScrollView(
          child: Column(
            children: [
              // Ensures that the column fills the viewport in the cross axis
              SizedBox(
                width: MediaQuery.of(context).size.width,
                height: MediaQuery.of(context).size.height * 0.1,
              ),
              // Use Flexible widgets around your content if needed to fill available space
              Flexible(
                flex: 0,
                child: Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      showSignUp ? SignUpContent(onToggleView: _toggleView) : SigninContent(onToggleView: _toggleView),
                    ],
                  ),
                ), // Flex of 0 means the child is inflexible and won't be forced to expand
              ),
              // You can add a SizedBox with a specific height if you want to ensure minimum scrollable area
              // Especially useful if your content doesn't fill the screen
              const SizedBox(height: 20), // Adjust the height to meet your design needs
            ],
          ),
        ),
      )
    );
  }

  void _toggleView() {
    setState(() {
      showSignUp = !showSignUp;
    });
  }
}

class SigninContent extends StatelessWidget {
  final VoidCallback onToggleView;

  const SigninContent({super.key, required this.onToggleView});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: const Color(0xFF3D6A71),
      width: 738,
      height: 368,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Login',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: TextField(
              decoration: InputDecoration(
                labelText: 'Username',
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(5)),
              ),
            ),
          ),
          const SizedBox(height: 20),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: TextField(
              decoration: InputDecoration(
                labelText: 'Password',
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(5)),
              ),
            ),
          ),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: () {},
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF34585E),
            ),
            child: const Text('Login'),
          ),
          TextButton(
            onPressed: onToggleView,
            child: const Text(
              'Sign up',
              style: TextStyle(color: Colors.white),
            ),
          ),
        ],
      ),
    );
  }
}

class SignUpContent extends StatelessWidget {
  final VoidCallback onToggleView;

  const SignUpContent({Key? key, required this.onToggleView}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      color: const Color(0xFF3D6A71),
      width: 738,
      height: 450, // Increased height to fit confirm password field
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: TextField(
              decoration: InputDecoration(
                labelText: 'Username',
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(5)),
              ),
            ),
          ),
          const SizedBox(height: 20),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: TextField(
              decoration: InputDecoration(
                labelText: 'Password',
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(5)),
              ),
            ),
          ),
          const SizedBox(height: 20),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),
            child: TextField(
              decoration: InputDecoration(
                labelText: 'Confirm Password',
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(5)),
              ),
            ),
          ),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: () {},
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF34585E),
            ),
            child: const Text('Sign up'),
          ),
          TextButton(
            onPressed: onToggleView,
            child: const Text(
              'Already have an account?',
              style: TextStyle(color: Colors.white),
            ),
          ),
        ],
      ),
    );
  }
}
