# Pentester at Owasp Juice Shop Application
## Scope and Objective

OWASP Juice Shop is an intentionally vulnerable web application designed to be used as a training platform for security testing and to practice vulnerability exploitation skills.

By using OWASP Juice Shop, one can learn to identify and exploit common vulnerabilities in web applications, such as SQL injection, command injection, cross-site scripting (XSS), and many others. Using a vulnerable application like OWASP Juice Shop, security testers can simulate real-world scenarios without compromising the security of production systems or confidential data. They can learn and practice how to exploit vulnerabilities and discover ways to mitigate and correct these issues in web applications.

Download and install the Juice Shop application.
```bash
  https://github.com/juice-shop/juice-shop
```

Web Reconnaissance
Web reconnaissance is one of the crucial stages in a penetration test (pentester). In this phase, directories, subdomains, emails owned by the application (prioritizing administrative emails), technologies used in website development, operating system fingerprint, analysis of /robots.txt, /sitemap.xml, login administrative panels, Google dorks, among other techniques and tools, are enumerated.
![screenshot](https://user-images.githubusercontent.com/102238044/235038359-38451dfe-f741-4827-a90c-e35ee66c8ba2.jpg)
Observing the page's behavior, a request is not processed by the server in a new route. Instead, routes are dynamically managed on the client side. In other words, a request does not cause the page to reload to another URL.

## Tip
Wappalyzer -> It is an extension that helps detect technologies used in the front-end of an application, such as front-end frameworks, JavaScript libraries, among others.
Use the developer tools in the browser and analyze whether the directives ng-content and ng-host are present. Usually, they are associated with a Single Page Application (SPA).
![screenshot](https://user-images.githubusercontent.com/102238044/235047454-0c1c56b0-53db-4a0a-8a17-845e24ae1863.jpg)

## Finding Routes in a SPA
Since routes are managed on the client side, they can be viewed in the browser's "debugger" tools. Knowing through Wappalyzer that it is a JavaScript application, let's search for the "path" routes.
![screenshot](https://user-images.githubusercontent.com/102238044/235059657-9697a6e2-fd3e-4dc7-9dbd-eded4e1e48b6.jpg)

## Email Enumeration
When making a request to an item in the Juice Shop, it sends a request to the API through an ID, which returns user comments. With this information, we can perform an email enumeration by passing a different ID number.
![screenshot](https://user-images.githubusercontent.com/102238044/236518510-d34de849-de28-4137-a7f5-4843867fbbbd.jpg)

Clone o repositório

```bash
  https://github.com/robertocoliver/Pentester_JuiceShop
```
Entre no diretório 
```bash
  cd Pentester_JuiceShop
```
Execute a ferramenta
```bash
  python3 mailenum.py
```
![screenshot](https://user-images.githubusercontent.com/102238044/236518553-a3749402-58ac-42c2-947c-09cdaaa924b8.jpg)

## Brute Force
On the login page, we check if the return code is triggered when an invalid password is submitted and if there is any lockout after a certain number of attempts. If there is no lockout policy on the login section, it is likely vulnerable to brute force attacks.

![Captura de tela_2023-05-05_14-08-52](https://user-images.githubusercontent.com/102238044/236523742-413a2d62-ae45-4b00-99eb-01b7ab57adb3.jpg)

Execute the tool
```bash
  python3 brute.py
```
![screenshot](https://user-images.githubusercontent.com/102238044/236518600-028dc9fe-8743-40f1-abb3-75eefa277db5.png)

## CORS (Cross-Origin Resource Sharing)
Another point to note is that the Access-Control-Allow-Origin directive is active with a value of "*", allowing API resources to be accessed by any other domain.

![screenshot](https://user-images.githubusercontent.com/102238044/236557530-ab11fdf4-05d0-46b5-a4c4-9f188aef5480.png)

Intercepting a Post Request for a Comment

![Captura de tela_2023-05-05_17-26-08](https://user-images.githubusercontent.com/102238044/236563217-3940eef1-92da-4ca6-bc21-78b69d6cc68b.jpg)

Changing the email of a user without privileges to that of an admin

![screenshot](https://user-images.githubusercontent.com/102238044/236563329-f8cd9d8c-f384-4e60-8307-0533ee3edd13.png)

Output:

![Captura de tela_2023-05-05_17-27-47](https://user-images.githubusercontent.com/102238044/236563796-a80db3e5-483e-4e56-955a-e3fe2d15a4d5.png)

## SQL Injection
To find SQL injection vulnerabilities (SQLi), it is necessary to test input fields in web applications, hidden fields in POST requests, HTTP headers, and cookies. The goal of the test is to identify which input fields are vulnerable to SQL injection attacks, allowing an attacker to execute malicious commands in the application's database.

Below, let's test the login page of the Juice Shop. A known email (admin or user) is submitted with a single or double quote.

![screenshot](https://user-images.githubusercontent.com/102238044/236584453-c67c256d-405c-481c-9212-eb0960ec2a2a.png)

The request made to the database generates a syntax error because the quotes were not closed. Subsequently, the website informs us that an error occurred and returns the database used along with the query.

```bash
  SELECT * FROM Users WHERE email = 'admin@juice-shp.op'' AND password = '202cb962ac59075b964b07152d234b70'
```
The next step for an attacker after interrupting the query is to make the rest of the query treated as a comment using --. This way, only the email is validated.
![screenshot](https://user-images.githubusercontent.com/102238044/236584458-7f841512-c916-4d23-a641-d0f1cf78c0df.png)

In the aforementioned example, it was used in the login and password parameters. However, as already mentioned, any user input, such as POST data, HTTP headers, and cookies, should be considered and addressed for correction in a web application.

## NOSQL Injection

Unlike relational databases that store data in a set of tables and columns, NoSQL, which stands for "not SQL," stores information in different structures and queries data differently from SQL. To determine which database an application uses, it is necessary to analyze how the application stores data. NoSQL uses JSON as a storage format, but there are many other options, such as XML, BSON, YAML, among others.

When intercepting a comment post, we have the following request:

 ```bash
  {"status":"success","data":
  {"product":"3","message":"x","author":"teste1@teste.com.br","likesCount":0,"likedBy":[],"_id":"ZgayhEWtBgPFzH68h","liked":true}]}
```
If the _id field that identifies an account is different from null $ne: 0, it returns all the _ids.

```bash
  {"_id":{"$ne": null}},"message":"ISSO É UM NOSQL"}
```
In this case, all "message" fields of all _ids would be modified at once.
 
## Cross Site Scripting (XSS)

In the OWASP XSS documentation, the methodology used for discovering XSS (Cross-Site Scripting) is through tests on form parameters, URL parameters, cookies, HTTP headers, and entries in logs and emails. Let's see:

Payload injected in the search parameter:
```bash
  <img src=a onerror="alert(1)">
```
![screenshot](https://user-images.githubusercontent.com/102238044/236903113-a4559fbe-3b10-46f3-9b52-fceb68dd2d0f.jpg)

Injecting payload and passing through a filter in the user feedback post:
```bash
  <<img src=a onerror="alert(1)">iframe src="javascript:alert('xss');">
```
![screenshot](https://user-images.githubusercontent.com/102238044/236903439-f5a9bcbe-6089-4c9e-8576-d97d1a61747c.png)
#
Payload executed for all users who view the comment:
#
![screenshot1](https://user-images.githubusercontent.com/102238044/236903450-7c80b5f4-3436-4224-b676-b609bf8aa859.png)

Email input
Creating an account and injecting the payload into the email field.

```bash
  "email":<iframe src=\"javascript:alert('xss')\">"
```
![screenshot](https://user-images.githubusercontent.com/102238044/236961083-34f938ec-9bb3-4f57-a298-283958f0a4d0.png)
#
Payload executed in the admin's administration directory
#
![screenshot](https://user-images.githubusercontent.com/102238044/236961102-233c2a85-e188-4f3d-a676-be80c8e8a08d.png)

## XML External Entities (XXE) in Practice

In an XML External Entities (XXE) attack, an attacker looks for inputs where they can upload .xml files. After finding the input, the hacker will test:
1. What extensions are accepted for file uploads?
2. Does the extension verification happen on the client side?
3. Does the file upload function perform any parsing?
4. Is there any bug, or does the site crash when uploading a file with an unauthorized extension?

Analyzing the application:
#
![screenshot](https://github.com/robertocoliver/Pentester_JuiceShop/assets/102238044/fcf8f849-ed3d-43e7-ab97-a1e98c22ec7e)
#
Injecting payload:
#
![screenshot](https://github.com/robertocoliver/Pentester_JuiceShop/assets/102238044/e1c30350-a15a-49ef-af22-e4c688d88ad3)

## Insecure Deserialization

For an attacker to find an Insecure Deserialization, it is essential to perform directory enumeration.

Directory brute force:
1. /ftp/package.json.bak used in Node.js to store project information and technologies used.

![screenshot](https://github.com/robertocoliver/Pentester_JuiceShop/assets/102238044/5ebf9aa5-1a41-4a88-b3f2-58aa2d35b7c6)

Injecting payload and bypassing the URL:
```bash
  http://127.0.0.1:3000/ftp/package.json.bak%2500.md
```
Brute Force diretórios de API: 

![screenshot](https://github.com/robertocoliver/Pentester_JuiceShop/assets/102238044/cdbacf69-6480-4435-8c6e-f7b502a6cc6c)
 
After finding an endpoint that makes API requests, an attacker would inject a payload so that, during deserialization, the code would be executed. Knowing that the application uses Node.js on the backend, we have the following payload:

```bash
  "(function teste(){while(true){}}())"
```
 ![screenshot](https://github.com/robertocoliver/Pentester_JuiceShop/assets/102238044/94da68c9-1834-4265-85d3-9e213fc68502)


## Exploiting Server-Side Template Injection (SSTI)
![screenshot](https://github.com/robertocoliver/Pentester_JuiceShop/assets/102238044/8c66fba2-2b75-4e2f-8d34-9278611091cb)
