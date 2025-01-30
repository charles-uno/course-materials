# Tech Industry Concepts

This is a rough idea for a course. It does not exist yet. Not sure if it ever will. The idea is:

- School focuses mostly on individual achievement, but most "real" software is written by teams. Prepare students to work productively as part of a team.
- The tech industry has made huge process improvements in recent decades. Pipelines vs manual deployments, agile vs waterfall, test-driven development. Expose students to these ideas and set them up to be a part of in ongoing forward movement.

# Course Structure

The course will be run as one big project.
Students will work together as a development team to create, maintain, and improve a web app.
Ideal enrollment is 3-10 advanced students. 

Students will begin by getting a proof-of-comcept app up and running.
Likely a browser-based game hosted on a CS lab machine.
Over the course of the semester they will roll out incremental improvements to the app, such as new features, UI improvements, automation, and/or telemetry.

This project will require significant collaboration between students.
They will have to divide work across the team, review each others' code changes, and navigate merge conflicts.
Students will be expected to keep notes about their own contributions as well as that of their teammates.
A significant portion of the course grade will be based on the peer reviews they write from these notes.

# Potential Topics 


## Team Dynamics

- Code reviews. Coding conventions. Style guides. Descriptive names for variables, methods, exceptions, data types. Merge conflicts. Enums. Cyclomatic complexity. 
- Agile workflow. Standups. Self-organizing teams. Product ownership. Responsiveness to stakeholders. Resilience to changing priorities. 
- Splitting up tasks to minimize people waiting on each other. Writing down milestones and comparing against them.
- Peer feedback. Keeping notes that make it easy to brag about yourself and others. Giving constructive feedback.
- Technical debt. What it is, when to take it on, and when to pay it down.
- Concept: you should expect to try on your own for X minutes/hours before interrupting someone else to ask for help. What is a reasonable number? How can you set up your project (code, docs, communication, etc) to facilitate finding answers? Everything should have a URL

## Reliability

- Concept: team/oncall. The people you work with should have a pretty good understanding of what your code does. This is important for effective code reviews. It's also important so your team doesn't call you on your day off!
- Unit tests, integration tests, API tests, mocks. Concept: you own the quality of your own work. Very inefficient to learn about a problem from a downstream team or user reports.
- Feature flags (aka killswitches). Deploying a big app with a bunch of tests can be slow. Deploying config files is fast. 
- Telemetry: counters, timers, structured logs (eg stack traces). Dashboards and alerts. 

## Pipelines and Deployment

- How hard is it for you to launch your code on a brand new server? Or 100 brand new servers? How sensitive are you to the exact specs of those servers? Pets vs cattle.
- Deploy on commit. Automated tests. Blue/green deployment. Probably some usage of GitHub Actions.
- Containers. Docker, Docker Compose, Kubernetes (probably just discussion, not hands-on)


## More...

- Privacy concerns. Collecting and retaining user data. 
- System design. Starting with a MVP, identifying bottlenecks, spitballing solutions. High-level understanding of client/server, load balancer, cache, database schema, etc. 
- Publisher/subscriber vs producer/consumer


# Readings

https://how.complexsystems.fail/

The DevOps Handbook


