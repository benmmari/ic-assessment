# ic-assessment
Engineering Assessment for IC

To run:
1. clone repository
2. cd into folder
3. npm install
4. docker-compose up

What I thought about the task:
This was my first time using Nameko and Docker. I was well aware of what docker was beforehand but I had never had to implement it myself before, so this was a great way for me to be exposed to it. I enjoyed the assessment a lot. I quickly figured out how to use and implement the technologies, however it took me a bit more time to get everything working together with Docker.

Pros and cons of the technology used in the task:

Pros:
Docker makes life a lot easier (less time and effort, reduced costs) when it comes to pulling down libraries/applications/dependancies and deploying software on different machines.
Containers can be provisioned very quickly and they are not as resource intensive as running individual virtual machines.
Nameko is extremely lightweight and easy to set up and even though it uses rabbbitmq it abstracts a lot of the integration details away from you.

Cons:
Initially, it takes time to implement tools such as Docker, and the time spent can certainly be justified if it pays of over the long run. But for simple services that will not be run on many machines or shared across teams, the time to implement it may seem counter productive. Containerization also comes with a number of inter-operability challenges, like maintaining proper networking between the containers.
Nameko requires rabbitmq in order to be fully functional (if you want to use rpc calls).


Design decisions:

The biggest challenge I had was trying to get my service to start after rabbitmq started.
What i ended up using was a combination of "depends_on" and"restart:always" and while this may not be the most elegant approach because the nameko service throws a "ECONNREFUSED" error a few times initially, it does work. An alternative approach would have been to use a more complex wrapper script, but I did not have the time to fully look into that. I also faced some errors around client vs server API complatability. Because Nameko rpc calls require a running rabbitmq installation, I decided to make use of docker compose to run a rabbitmq container alongside my service container. I included a config.yaml file because I needed to get my service to communicate with rabbitmq  which was running in a different container, in this config file there is the rabbitmq URI which points to 'rabbitmq' (the name of the service) as the host name instead of the conventional 127.0.0.1. I used the zlib for compression.


Research breakdown:

Nameko research and implementation: ~4 hours
Docker research and implementation: ~8 hours
Documentation: ~1 hour

