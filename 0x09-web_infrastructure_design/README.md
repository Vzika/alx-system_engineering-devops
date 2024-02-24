0-simple_web_stac

Infrastructure Design:

Server:

This is a physical or virtual machine (let's call it FoobarServer) where all components of your web infrastructure will be installed.
Web Server (Nginx):

Nginx will be responsible for handling incoming web requests. It listens for requests from users and directs them to the appropriate resources on the server.
Application Server:

The application server (let's call it FoobarAppServer) runs the actual code that generates dynamic content for your website. It processes requests, interacts with the database, and sends responses back to the web server.
Application Files (Your Code Base):

These are the files containing the code for your website. They reside on the FoobarServer and are processed by the application server to generate dynamic content.
Database (MySQL):

MySQL will store and manage the data for your website. This can include user information, content, and other relevant data.
Domain Name (www.foobar.com):

A domain name is like the address of your website on the internet. In this case, www.foobar.com is configured to point to the IP address of your server (8.8.8.8).
Specifics about the Infrastructure:

What is a server?

A server is a computer or system that provides services to other computers, known as clients. In this case, FoobarServer is the computer hosting your website.
Role of the domain name:

The domain name (www.foobar.com) serves as a human-readable address for your website. It helps users access your site without needing to remember the server's IP address.
DNS record type for www.foobar.com:

The DNS record type for www.foobar.com is a CNAME (Canonical Name) record, which points to the domain's actual hostname.
Role of the web server:

The web server (Nginx) handles incoming HTTP requests from users' browsers and directs them to the appropriate resources on the server, such as static files or the application server.
Role of the application server:

The application server (FoobarAppServer) runs the dynamic code of your website. It processes user requests, interacts with the database, and generates the content that the web server sends back to the user's browser.
Role of the database:

MySQL serves as the database where your website stores and retrieves data. It can include user information, posts, or any other data required for your website.
Communication between server and user's computer:

The communication between the server and the user's computer happens over the internet using the HTTP or HTTPS protocols. The web server sends the requested content back to the user's browser.
Issues with this Infrastructure:

Single Point of Failure (SPOF):

This infrastructure has a single server, making it vulnerable to a single point of failure. If the server goes down, the entire website becomes inaccessible.
Downtime during maintenance:

When maintenance, updates, or code deployment is needed, the web server might need to be restarted, causing downtime for users trying to access the site.
Scaling limitations:

This infrastructure is not easily scalable. If there's a sudden surge in incoming traffic, a single server might not handle the load efficiently.


1-distributed_web_infrastructure:

 For every additional element, why you are adding it:
Load Balancer (HAproxy): Added to distribute incoming web traffic across multiple servers. This ensures that no single server is overwhelmed, improving performance and providing fault tolerance.

Server 1 and Server 2: Multiple servers are added to handle more users simultaneously and to provide redundancy. If one server fails, the other can still handle requests.

Database (MySQL) with Primary-Replica Cluster: Introducing a database cluster provides redundancy and improves read scalability. The primary database handles write operations, and the replica database ensures data availability for read operations.

2. Distribution algorithm your load balancer is configured with and how it works:
Distribution Algorithm (e.g., Round Robin): Determines how the load balancer assigns incoming requests to the available servers. For example, Round Robin distributes requests equally among the servers in a circular order.
3. Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both:
Active-Active Setup: Both servers actively handle requests simultaneously. This setup provides load balancing and redundancy, with each server capable of handling user requests independently.

Active-Passive Setup: Only one server actively handles requests at a time, while the other remains on standby. If the active server fails, the passive server takes over. This setup provides redundancy but may not utilize resources as efficiently as Active-Active.

4. How a database Primary-Replica (Master-Slave) cluster works:
Primary-Replica Cluster: In a Primary-Replica (or Master-Slave) configuration, there is a primary database (master) and one or more replica databases (slaves).

Write Operations (Primary): The primary database handles write operations (insert, update, delete). Any changes to the data occur on the primary first.

Read Operations (Replica): The replica databases replicate data from the primary and handle read operations. This improves read performance and provides redundancy.

5. What is the difference between the Primary node and the Replica node in regard to the application:
Primary Node: Responsible for handling write operations, ensuring data consistency and integrity. It's the authoritative source for data changes.

Replica Node: Handles read operations, serving as a copy of the primary data. It enhances read performance, provides fault tolerance, and can be used for backup purposes. However, it may have a slight delay in receiving updates compared to the primary.

2-secured_and_monitored_web_infrastructure

Firewalls:

Why: Firewalls are added to control and filter network traffic between the different components of the infrastructure. They serve as a barrier to prevent unauthorized access, protect against malicious attacks, and enforce security policies. Firewalls are crucial for maintaining the integrity and security of the network.
SSL Certificate and HTTPS:

Why: SSL certificates and HTTPS (HTTP Secure) are implemented to encrypt the communication between clients and the web servers. This encryption ensures the confidentiality and integrity of data in transit. It prevents eavesdropping, data tampering, and man-in-the-middle attacks, enhancing the overall security of the website.
Monitoring:

Why: Monitoring is used to track the performance, availability, and health of the entire web infrastructure. It helps in identifying and addressing issues before they impact users. Monitoring is essential for proactive problem resolution, capacity planning, and optimizing the overall performance and user experience.
Monitoring Tool Data Collection:

How: Monitoring tools utilize agents or collectors deployed on servers to collect various types of data. These agents gather information such as system metrics (CPU usage, memory, disk I/O), application logs, network performance, and more. The collected data is then transmitted to a centralized monitoring platform for analysis and reporting.
Monitoring Web Server QPS:

What to do: To monitor the Query Per Second (QPS) of a web server, configure monitoring tools to track metrics related to web server performance. This includes monitoring the server's response time, request rate, and other relevant metrics. If QPS is high and approaching the server's capacity, consider scaling resources, optimizing code, or distributing traffic more efficiently through load balancing.

In summary, each element is added to the infrastructure to fulfill specific purposes: firewalls for security, SSL/HTTPS for encrypted communication, monitoring for performance and health tracking, and monitoring tools for data collection and analysis. Monitoring web server QPS involves setting up tools to track and analyze relevant metrics to ensure optimal performance.


Terminating SSL at the Load Balancer:

Issue: When SSL termination occurs at the load balancer, communication between the load balancer and web servers is unencrypted. This exposes sensitive data to potential security risks during internal communication. If an attacker gains access to the internal network, they could eavesdrop on or tamper with the unencrypted data flowing between the load balancer and web servers.
Solution: Implement end-to-end encryption by using SSL certificates not only at the load balancer but also on the web servers. This ensures that data is encrypted throughout the entire communication path, providing a higher level of security.
Single MySQL Server for Writes:

Issue: Having only one MySQL server capable of accepting writes creates a single point of failure for write operations. If this server goes down or experiences issues, write operations will fail, impacting the availability and functionality of the entire system.
Solution: Implement database clustering, replication, or sharding to distribute write operations across multiple MySQL servers. This enhances fault tolerance and ensures that the system can continue to handle write requests even if one server is unavailable.
Servers with Identical Components:

Issue: Using servers with identical components (database, web server, and application server) across the infrastructure poses a risk of systemic failure. If a flaw, vulnerability, or bug affects one component, it can potentially impact all servers simultaneously. This lack of diversity increases the likelihood of widespread outages or security breaches.
Solution: Diversify the components across servers, ensuring that a failure in one area does not cascade across the entire infrastructure. Use load balancing to distribute traffic and ensure that no single server is a critical point of failure. This approach improves redundancy and fault tolerance.
