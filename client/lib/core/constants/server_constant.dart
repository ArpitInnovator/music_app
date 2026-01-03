import 'package:flutter/foundation.dart';
import 'dart:io' show Platform;

class ServerConstant {
  static String get serverURL {
    if (kIsWeb) {
      return 'http://localhost:8000';
    }

    // Android Emulator
    if (Platform.isAndroid) {
      return 'http://192.168.29.33:8000';
    }

    // Fallback (iOS / others)
    return 'http://localhost:8000';
  }
}
