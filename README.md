QUESTION ONE
Scenario:
A large retail company relies on a Python-based application to manage and track product information, sales, and customer interactions. The software development team is responsible for maintaining this application and ensuring it performs reliably and securely even as new features are added.
a)	Write Python code that uses multiple classes to perform basic calculations and apply discounts to product prices. Briefly describe and generate Python code and explain the purpose of using inheritance and encapsulation in these classes. Use the last two values of your student number as the input for variables in Product to showcase expected outputs.								(20 Marks)	
b)	With the help of a code snippet in relation to the case scenario above Explain the importance of regression testing in ensuring that the application remains stable with continuous updates, especially in critical modules such as data processing and price management.								(15 Marks)
c)	Rewrite the code for the scenario above to include visualization using libraries like Matplotlib or Plotly. Visualize both input and output data for an item’s price before and after a discount is applied.						(15 Marks)
QUESTION TWO
Based on the scenario above the retail company’s software development team is tasked with creating a secure e-commerce site using Django. They are concerned about security threats common to web applications, including session hijacking, cross-site scripting, SQL injection, buffer overflows, and CSRF.
a)	Briefly explain with the help of simple code snippets with relation to the case scenario the following Object-Oriented Programming concepts and their importance in structuring code for large applications:					(20 Marks)
i.	Inheritance
ii.	Encapsulation
iii.	Polymorphism
b)	Develop Django code snippets to demonstrate a secure design using the MVC framework. Make sure you Use Django’s built-in functions and best practices to show how these vulnerabilities can be mitigated. 				(30 Marks)
o	Security Aspects to Address:
1.	Session Hijacking – Implement Django’s SESSION_COOKIE_SECURE and SESSION_EXPIRE_AT_BROWSER_CLOSE settings to limit session exposure. Use secure cookie settings and session expiry.
2.	Cross-Site Scripting (XSS) – Show how to use Django’s autoescape functionality in templates to prevent XSS.  Sanitize all inputs and use Django’s {{ variable|safe }} sparingly.
3.	SQL Injection – Use Django ORM’s parameterized queries to avoid SQL injection. Explain and show how the Django ORM helps prevent direct SQL injections.
4.	Buffer Overflows – Although Python limits direct buffer overflow attacks, show input validation techniques to prevent excessive data handling.
5.	CSRF (Cross-site Request Forgery) – Enable Django’s CSRF protection middleware. Illustrate using Django’s CSRF token protection.



![Uploading image.png…]()
