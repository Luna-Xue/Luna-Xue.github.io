---
toc: true
---
## xApps Overview

xApps are applications that run on the O-RAN Near-Real-Time RAN Intelligent Controller, usually called the Near-RT RIC. They provide programmable control, optimization, and monitoring of radio access network behavior on near-real-time timescales, typically from about 10 milliseconds to 1 second.

In an O-RAN deployment, the Near-RT RIC sits between the service management/orchestration layer and the RAN nodes. xApps use RIC platform services to subscribe to measurements, receive events from E2 nodes such as O-CU and O-DU components, and send control or policy actions back through the E2 interface. This makes it possible to implement custom RAN intelligence without modifying the base station software directly.

Common xApp use cases include traffic steering, interference management, mobility optimization, anomaly detection, quality-of-service control, and AI/ML-driven radio resource management. Each xApp is usually packaged as a deployable service and interacts with the RIC through messaging, APIs, configuration files, and subscriptions.

### Python-Based xApps

These docs focus on Python-based xApps. In the O-RAN SC ecosystem, the Python xApp framework helps reduce repeated boilerplate by providing common support for RIC Message Router communication, Shared Data Layer access, application startup, and health-check behavior.

The framework does not replace the application logic. The developer still defines what the xApp should monitor, how it should process incoming data, and what action it should take. The framework mainly provides the structure around that logic so the xApp can communicate with the Near-RT RIC platform.

### Reactive xApps

A reactive xApp runs in response to messages delivered through RMR. The application registers callback functions for the message types it expects, and the framework invokes the matching callback when a message arrives.

This model is useful when the xApp should act only after receiving a RIC indication, subscription response, control acknowledgement, or other message from the platform. A default callback is also typically defined so unexpected message types can be handled safely.

### General xApps

A general xApp runs according to its own application loop. It may still read RMR messages, use SDL, or call other services, but it is not limited to message-triggered callbacks.

This model is useful for xApps that need to periodically check state, run a continuous control loop, coordinate multiple data sources, or perform background tasks in addition to handling RIC messages.

### Core xApp Components

Most Python xApps include a few common components:

- **Application logic:** the control, monitoring, analytics, or AI/ML logic that defines the xApp behavior.
- **RMR messaging:** the message interface used to send and receive RIC platform messages.
- **Subscriptions:** the mechanism used to request specific RAN measurements or event streams from E2 nodes.
- **Configuration:** deployment-time settings such as message types, service ports, routes, policies, and runtime parameters.
- **Shared state:** optional use of services such as the Shared Data Layer for storing or retrieving information needed by the xApp.
- **Health checks:** probes or handlers that help the platform determine whether the xApp is running and able to communicate correctly.

