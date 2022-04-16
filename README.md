**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation
### The Default namespace installation
![The Default namespace installation](answer-img/01-Kubectl-Namespace-Default.png)

### The Monitoring namespace installation
![The Monitoring namespace installation](answer-img/01-Kubectl-Namespace-Monitoring.png)

### The Observability namespace installation
![The Observability namespace installation](answer-img/01-Kubectl-Namespace-Observability.png)

## Setup the Jaeger and Prometheus source
### Grafana Home Page and Data Source Configuration
![Grafana Home Page and Data Source Configuration](answer-img/02-Grafana-Home&DataSources.png)


## Create a Basic Dashboard
### Simple Dashboard with Prometheus as a source
![Simple Dashboard with Prometheus as a source](answer-img/03-Grafana-Prometheus-as-a-Source.png)

## Describe SLO/SLI
### Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

SLI is an artifact that collects information and is used to measure availability.
SLIs could measure uptime, latency, or the proportion between success interactions for a specific period of time e.g. week, month; that means. We will aggregate interactions that don’t throw an exception or return an HTTP error or take more than a specific period of time to produce a result and define error policies as a playbook to reduce the likelihood or mitigate future problems.

## Creating SLI metrics.
### It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
*TODO:*

## Create a Dashboard to measure our SLIs
### Dashboard Uptime Backend to 24hs
![Dashboard Uptime Backend to 24hs](answer-img/04-Uptime-Backend-24hs.png)

### Dashboard Uptime Frontend to 24hs
![Dashboard Uptime Frontend to 24hs](answer-img/04-Uptime-Frontend-24hs.png)

### Dashboards 40x and 50x Errors
![Dashboard 40x and 50x Errors](answer-img/04-Errors-40x&50x-24hs.png)

### Dashboards Uptime and Errors
![Dashboard Uptime and Errors](answer-img/04-Dashboards-Uptime&Errors-24hs.png)


## Tracing our Flask App
### Trace Python Code - Part 1
![Trace Python Code - Part 1](answer-img/05-Tracing-Code-01.png)

### Trace Python Code - Part 2
![Trace Python Code - Part 2](answer-img/05-Tracing-Code-02.png)

### Jaeger in Panel
![Jaeger in Panel](answer-img/05-Tracing-Jaeger.png)

## Jaeger in Dashboards
### Dashboard Grafana as a Jaeger Source - Part 1
![Dashboard Grafana as a Jaeger Source - Part 1](answer-img/06-Jaeger-Dashboards-Grafana-01.png)

### Dashboard Grafana as a Jaeger Source - Part 2
![Dashboard Grafana as a Jaeger Source - Part 2](answer-img/06-Jaeger-Dashboards-Grafana-02.png)


## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

### TROUBLE TICKET

- Name: Application temporary unavailable
- Date: 15/04/2022
- Subject: Service Unavailable
- Affected Area: Backend - /api
- Severity: 7.0 - High
- Description: The application is unstable and frequently showing the follow message: Service Unavailable. Please contact the System Admnistrator.


## Creating SLIs and SLOs
SLO: The Applications need to have a 99.95% uptime per month. 
SLI:
- CPU Saturation (Saturation)
- how many error messages we are seeing (Errors)
- how many success messages we are seeing (Success)
- Request Response time of the Apis (Latency)

## Building KPIs for our plan
1. SLI: Total successful http requests is more than or equal to 99.95% in a month
2. SLI: Total failing http requests is less than or equal to 0.05% in a month (40x and 50x)
3. SLI: The CPU usage up till 75%
4. SLI: The Memory usage up till 50%

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
