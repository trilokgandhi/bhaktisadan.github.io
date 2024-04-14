/*
1. Develop a java application using concept of JDBC for user login. User will enter
username and password. Application will match for the same in database table. If match
is found then display message "Successful Login" and if not found then display message
"Invalid Username and password .
*/
import java.sql.*;
import java.util.Scanner;

public class GetData {
public static void main(String[] args) {
try{
Scanner sc = new Scanner(System.in);
System.out.println("Enter Username :");
String username = sc.nextLine();
System.out.println("Enter Password :");
String password = sc.nextLine();
Class.forName("com.mysql.cj.jdbc.Driver");
Connection con =
DriverManager.getConnection("jdbc:mysql://localhost:3306/parul","root","");
Statement st = con.createStatement();
ResultSet rs= st.executeQuery("SELECT * FROM `user` where
username='"+username+"' and password='"+password+"'");
if(rs.next()){
System.out.println("Login Successful");
}
else{
System.out.println("Invalid Username and password");
}
con.close();
}
catch (Exception e){
e.printStackTrace();
}
}
}

/*
2 Develop a Menu driven java application for student information which will create the table
with appropriate columns. Menu will contain the options like insert, update and delete.
Based on the option, data will be inserted or updated or deleted from table based on
student id (student_id will be primary key). Display appropriate message for each
operation.
*/
import java.sql.*;
import java.util.Scanner;

public class StudentInformation {
public static void main(String[] args) {
Connection con = null;
PreparedStatement ps = null;
Scanner sc = new Scanner(System.in);
try {
Class.forName("com.mysql.cj.jdbc.Driver");
con = DriverManager.getConnection("jdbc:mysql://localhost:3306/parul", "root", "");
String sid;
String sname;
String sage;
String grade;
System.out.println("Menu:");
System.out.println("1. Insert Student");
System.out.println("2. Update Student");
System.out.println("3. Delete Student");
System.out.println("4. Show Students");
System.out.println("5. Exit");
int choice;
do {
System.out.print("Enter your choice (1-5): ");
String userChoice = sc.nextLine();
choice = Integer.parseInt(userChoice);
switch (choice) {
case 1:
System.out.print("Enter Student Name : ");
sname = sc.nextLine();
System.out.print("Enter Student age : ");
sage = sc.nextLine();
System.out.print("Enter Student grade : ");
grade = sc.nextLine();
ps = con.prepareStatement(" INSERT INTO `student`( `name`, `age`, `grade`)
VALUES (?,?,?)");
ps.setString(1, sname);
ps.setString(2, sage);
ps.setString(3, grade);
int count = ps.executeUpdate();
if (count > 0) {
System.out.println("Data Inserted ");
} else {
System.out.println("Data NOT Inserted ");
}
break;
case 2:
System.out.print("Enter Student ID : ");
sid = sc.nextLine();
System.out.print("Enter Student Name : ");
sname = sc.nextLine();
System.out.print("Enter Student age : ");
sage = sc.nextLine();
System.out.print("Enter Student grade : ");
grade = sc.nextLine();
ps = con.prepareStatement("UPDATE `student` SET
`name`=?,`age`=?,`grade`=? WHERE `student_id`=?");
ps.setString(1, sname);
ps.setString(2, sage);
ps.setString(3, grade);
ps.setString(4, sid);
count = ps.executeUpdate();
if (count > 0) {
System.out.println("Data Updated ");
} else {
System.out.println("Data NOT Updated, Please Enter Correct Student ID");
}
break;
case 3:
System.out.print("Enter Student ID : ");
sid = sc.nextLine();
ps = con.prepareStatement("DELETE FROM `student` WHERE `student_id`=?");
ps.setString(1, sid);
count = ps.executeUpdate();
if (count > 0) {
System.out.println("Data Deleted ");
} else {
System.out.println("Data NOT Deleted, Please Enter Correct Student ID");
}
break;
case 4:
ps = con.prepareStatement("SELECT * FROM `student`");
ResultSet rs = ps.executeQuery();
if (rs.next()) {
System.out.println("Student ID : " +rs.getString(1) + " Student Name : "
+rs.getString(2)+ " Student age : " +rs.getString(3) + " Student Grade : " +rs.getString(4));
} else {
System.out.println("NO Records Found");
}
break;
case 5:
System.out.println("byeee!");
break;
default:
System.out.println("Invalid choice. Please enter a number between 1 and 4.");
break;
}
} while (choice != 5);
} catch (Exception e) {
e.printStackTrace();
}
}
}

/*
3 Develop an application using GUI for user registration. In first form user will enter the
data for registration (e.g. Name, Birthdate, Email_id, Phone_No). When user clicks on
submit button, data will be inserted into database and user will be redirected to another
form. In this form data will be selected from database and displayed in proper format.
*/
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class Registration {
static JFrame registrationFrame;
static JFrame displayFrame;
static JTextField nameField, birthdateField, emailField, phoneField;
static JButton submitButton;
public static void main(String[] args) {
SwingUtilities.invokeLater(() -> {
try {
registrationFrame = new JFrame("User Registration");
registrationFrame.setSize(400, 300);
registrationFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
JPanel panel = new JPanel();
panel.setLayout(new GridLayout(5, 2));
panel.add(new JLabel("Name:"));
nameField = new JTextField();
panel.add(nameField);
panel.add(new JLabel("Birthdate:"));
birthdateField = new JTextField();
panel.add(birthdateField);
panel.add(new JLabel("Email ID:"));
emailField = new JTextField();
panel.add(emailField);
panel.add(new JLabel("Phone Number:"));
phoneField = new JTextField();
panel.add(phoneField);
submitButton = new JButton("Submit");
submitButton.addActionListener(new ActionListener() {
@Override
public void actionPerformed(ActionEvent ae) {
try{ Class.forName("com.mysql.cj.jdbc.Driver");
Connection con =
DriverManager.getConnection("jdbc:mysql://localhost:3306/parul", "root", "");
PreparedStatement ps = con.prepareStatement("INSERT INTO users (name,
birthdate, email, phone) VALUES (?, ?, ?, ?)");
ps.setString(1, nameField.getText());
ps.setString(2, birthdateField.getText());
ps.setString(3, emailField.getText());
ps.setString(4, phoneField.getText());
int count = ps.executeUpdate();
registrationFrame.setVisible(false);
displayFrame = new JFrame("User Data Display");
displayFrame.setSize(400, 300);
displayFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
JTextArea displayArea = new JTextArea();
displayArea.setEditable(false);
if (count > 0) {
ps = con.prepareStatement("SELECT * FROM users");
ResultSet rs = ps.executeQuery();
while (rs.next()) {
displayArea.append("User ID: " + rs.getString(1) + "\n");
displayArea.append("Name: " + rs.getString(2) + "\n");
displayArea.append("Birthdate: " + rs.getString(3) + "\n");
displayArea.append("Email: " + rs.getString(4) + "\n");
displayArea.append("Phone: " + rs.getString(5) + "\n\n");
}
displayFrame.getContentPane().add(new JScrollPane(displayArea));
displayFrame.setVisible(true);
} else {
displayArea.append(" NO DATA \n");
}
} catch (Exception e) {
e.printStackTrace();
}
}
});
panel.add(submitButton);
registrationFrame.getContentPane().add(BorderLayout.CENTER, panel);
registrationFrame.setVisible(true);
} catch (Exception e) {
e.printStackTrace();
}
});
}
}

/*MyServlet.java*/
package com.mycompany.diveservlet;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.IOException;
import java.io.PrintWriter;
import jdk.internal.org.jline.reader.PrintAboveWriter;

public class MyServlet extends HttpServlet {
@Override
protected void service(HttpServletRequest req, HttpServletResponse resp) throws
ServletException, IOException {
PrintWriter out = resp.getWriter();
out.println("<h1> Hello Service method </h1>");
}
}

/*4 Develop a data driven servlet application for user authentication.*/
Index.html
<!DOCTYPE html>
<html>
<head>
<title>Start Page</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
<h1>Hello Servlet!</h1>
<form action="MyServlet" method="GET">
User name : <input type="text" name="username"> <br><!-- comment -->
Password : <input type="text" name="password"> <br><!-- comment -->
<input type="submit" name="submit">
</form>
</body>
</html>

MyServlet.java
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;
import java.sql.*;

public class MyServlet extends HttpServlet {
@Override
protected void service(HttpServletRequest req, HttpServletResponse resp) throws
ServletException, IOException {
PrintWriter out = resp.getWriter();
out.println("<h1> Hello from Service method </h1>");
String uname = req.getParameter("username");
String pass = req.getParameter("password");
out.println(uname);
out.println(pass);
try{ Class.forName("com.mysql.cj.jdbc.Driver");
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/parul",
"root", "");
Statement st = con.createStatement();
ResultSet rs = st.executeQuery("SELECT * FROM `user` where username='" + uname +
"' and password='" + pass + "'");
if (rs.next()) {
out.println("Login Successful");
} else {
out.println("Invalid Username and password");
}
con.close();
} catch (Exception e) {
out.println("There was some problem");
}
}
}

/*5 Develop a servlet application for implementing student grading system. In this system on
first page student will enter his data (name, id and department). By clicking on next
button he will be redirected to another page. On the second page he will enter marks of
all 6 subjects. By clicking on "Generate result" he will be redirected to next page. On this
page all information of student will be displayed along with the result (pass or fail) in
appropriate color. Also display the name of student on each page he visits. (Use session
management)*/
firstPage.html
<html>
<head>
<title>TODO supply a title</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<form action="Servlet1" method="GET">
Enrollment number : <input type="text" name="enno"> </br>
Name : <input type="text" name="name"> </br>
Department : <input type="text" name="department"> </br>
<input type="submit" value="next" name="submit"/>
</form>
</body>
</html>

subjectMarks.html
<html>
<head>
<title>TODO supply a title</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<form action="Servlet2" method="GET">
Subject 1 : <input type="text" name="sub1"> </br>
Subject 2 : <input type="text" name="sub2"> </br>
Subject 3 : <input type="text" name="sub3"> </br>
Subject 4 : <input type="text" name="sub4"> </br>
Subject 5 : <input type="text" name="sub5"> </br>
Subject 6 : <input type="text" name="sub6"> </br>
<input type="submit" value="Generate Result" name="submit"/>
</form>
</body>
</html>

Servlet1.java
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;

public class Servlet1 extends HttpServlet {
@Override
protected void service(HttpServletRequest req, HttpServletResponse resp) throws
ServletException, IOException {
String enno = req.getParameter("enno");
String name = req.getParameter("name");
String department = req.getParameter("department");
HttpSession session = req.getSession();
session.setAttribute("enno", enno);
session.setAttribute("name", name);
session.setAttribute("department", department);
RequestDispatcher rd = req.getRequestDispatcher("/subjectMarks.html");
rd.include(req, resp);
}
}

Servlet2.java
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.*;

public class Servlet2 extends HttpServlet {
@Override
protected void service(HttpServletRequest req, HttpServletResponse resp) throws
ServletException, IOException {
double sub1 = Double.parseDouble(req.getParameter("sub1"));
double sub2 = Double.parseDouble(req.getParameter("sub2"));
double sub3 = Double.parseDouble(req.getParameter("sub3"));
double sub4 = Double.parseDouble(req.getParameter("sub4"));
double sub5 = Double.parseDouble(req.getParameter("sub5"));
double sub6 = Double.parseDouble(req.getParameter("sub6"));
HttpSession session = req.getSession();
String enno = (String) session.getAttribute("enno");
String name = (String) session.getAttribute("name");
String department = (String) session.getAttribute("department");
resp.setContentType("text/html");
PrintWriter out = resp.getWriter();
out.println("<h3> Enrollment number : " + enno + "</h3>");
out.println("<h3> Name : " + name + " </h3>");
out.println("<h3> department : " + department + " </h3>");
out.println("<h2> sub1 : " + sub1 + " </h2>");
out.println("<h2> sub2 : " + sub2 + " </h2>");
out.println("<h2> sub3 : " + sub3 + " </h2>");
out.println("<h2> sub4 : " + sub4 + " </h2>");
out.println("<h2> sub5 : " + sub5 + " </h2>");
out.println("<h2> sub6 : " + sub6 + " </h2>");
if (sub1 >= 30 && sub2 >= 30 && sub3 >= 30 && sub4 >= 30 && sub5 >= 30 && sub6 >=
30) {
out.print("<h1> PASS </h1>");
} else {
out.print("<h1> FAIL </h1>");
}
}
}

/*6 User should be redirected to the URL entered in location text box.*/
<html>
<head>
<title>TODO supply a title</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<form action="url">
Enter URL : <input type="text" name="url"> </br>
<input type="submit" name="submit" value="GO">
</form>
</body>
</html>

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import java.io.IOException;

public class Practical6 extends HttpServlet {
@Override
protected void service(HttpServletRequest req, HttpServletResponse resp) throws
ServletException, IOException {
String str = req.getParameter("url");
resp.sendRedirect(str);
}
}