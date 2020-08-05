import 'dart:convert';

import 'package:http/http.dart' as http;
// import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'models.dart';

class User {
  final String URL = 'http://192.168.31.188:7869/api/';
  Future<String> authtoken;
  Student student;
  User(this.authtoken) {
    this.student = _loadStudent();
  }

  User.fromEmailPasswrod({String email, String password}) {
    authtoken = _login(email, password);
    this.student = _loadStudent();
  }

  Future<String> _login(String email, String password) async {
    Map<String, String> payload = {'username': email, 'password': password};
    var response = await http.post('${this.URL}auth/', body: payload, headers: {});
    var jsonData = json.decode(response.body);

    return jsonData['token'];
  }

  dynamic _loadStudent() async {
    var response =
        await http.get('${this.URL}student', headers: {'Authorization': 'Token ${this.authtoken}'});
    Map jsonData = jsonDecode(response.body);
    print(jsonData);
    return Student();
  }
}

void main() {
  User user =
      User.fromEmailPasswrod(email: "adityapal2000.2013@gmail.com", password: "aditya.com1");
  print(user.student);
}
