import 'dart:io';

import 'package:camera/camera.dart';
import 'package:camera_platform_interface/src/types/camera_description.dart';
import 'package:flutter/material.dart';

import 'gallery_screen.dart';

class CameraScreen extends StatefulWidget {
  final List<CameraDescription> cameras;

  const CameraScreen({Key? key, required this.cameras}) : super(key: key);

  @override
  State<CameraScreen> createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;
  int selectedCamera = 0;
  List<File> capturedImages = [];

  initializeCamera(int cameraIndex) async {
    _controller =
        CameraController(widget.cameras[cameraIndex], ResolutionPreset.medium);
    _initializeControllerFuture = _controller.initialize();
  }

  @override
  void initState() {
    initializeCamera(selectedCamera);
    super.initState();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.max,
      children: [
        Expanded(
          flex: 8,
          child: FutureBuilder<void>(
            future: _initializeControllerFuture,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                // If the Future is complete, display the preview.
                return CameraPreview(_controller);
              } else {
                // Otherwise, display a loading indicator.
                return const Center(child: CircularProgressIndicator());
              }
            },
          ),
        ),
        Expanded(
          flex: 2,
          child: Row(
            mainAxisSize: MainAxisSize.max,
            children: [
/*
              Container(
                child: IconButton(
                  onPressed: () {
                    if (widget.cameras.length > 1) {
                      setState(() {
                        selectedCamera =
                            selectedCamera == 0 ? 1 : 0; //Switch camera
                        initializeCamera(selectedCamera);
                      });
                    } else {
                      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                        content: Text('No secondary camera found'),
                        duration: const Duration(seconds: 2),
                      ));
                    }
                  },
                  icon: Icon(Icons.switch_camera_rounded, color: Colors.white),
                ),
              ),
*/
              Expanded(
                flex: 1,
                child: GestureDetector(
                  onTap: () async {
                    if (widget.cameras.length > 1) {
                      setState(() {
                        selectedCamera =
                        selectedCamera == 0 ? 1 : 0; //Switch camera
                        initializeCamera(selectedCamera);
                      });
                    } else {
                      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                        content: Text('No secondary camera found'),
                        duration: const Duration(seconds: 2),
                      ));
                    }
                  },
                  child: Icon(Icons.switch_camera_rounded, color: Colors.white),
                ),
              ),
              Expanded(
                flex: 1,
                child: GestureDetector(
                  onTap: () async {
                    await _initializeControllerFuture; //To make sure camera is initialized
                    var xFile = await _controller.takePicture();
                    setState(() {
                      capturedImages.add(File(xFile.path));
                    });
                  },
                  child: Container(
                    height: 60,
                    width: 60,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: Colors.white,
                    ),
                  ),
                ),
              ),
              Expanded(
                flex: 1,
                child: Center(
                  child: GestureDetector(
                    onTap: () {
                      if (capturedImages.isEmpty) return; //Return if no image
                    Navigator.push(context,
                          MaterialPageRoute(
                              builder: (context) => GalleryScreen(
                                  images: capturedImages.reversed.toList())));
                    },
                    child: Container(
                      height: 60,
                      width: 60,
                      decoration: BoxDecoration(
                        border: Border.all(color: Colors.white),
                        image: capturedImages.isNotEmpty
                            ? DecorationImage(image: FileImage(capturedImages.last), fit: BoxFit.cover)
                            : null,
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
        )
      ],
    );
  }
}
