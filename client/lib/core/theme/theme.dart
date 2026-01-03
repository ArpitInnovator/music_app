import 'package:client/core/theme/app_pallete.dart';
import 'package:flutter/material.dart';

class AppTheme {

  static OutlineInputBorder _boarder(Color color) =>  OutlineInputBorder(
        borderSide: BorderSide(
          color: color,
          width: 3 ,
        ),
        borderRadius: BorderRadius.circular(10)
      );

  static final darkThemeMode = ThemeData.dark().copyWith(
    scaffoldBackgroundColor: Pallete.backgroundColor,
    inputDecorationTheme:  InputDecorationTheme(
      contentPadding: EdgeInsets.all(27),
      enabledBorder: _boarder(Pallete.borderColor) ,
      focusedBorder: _boarder(Pallete.gradient2) ,
    ),
    bottomNavigationBarTheme: BottomNavigationBarThemeData(
       backgroundColor: Pallete.backgroundColor,
    ),
  );
}
