# deployment-pipeline-challenge
For the 'The Anatomy of a Deployment Pipeline' course by Continuous Delivery Ltd

## Overview
This is a dashboard that will show the status of the orders for customers (like in a lobby). Imagine that there is a different system that's actually processing the food orders, and it is creating logs of the food orders. The logs are what will be used to populate the dashboard. 

## Local Running

```
docker-compose build
docker-compose up
```

## Test Running

Refer to .github/workflows for how to run the tests.

## Slicing
### Current focus/use case:
Customer can identify when food order has started processing

### Current vertical slice:
- Simplest UI: Table showing
- Simplest logic: API that transforms the logs into a list that the table can show easily
- Simplest storage: Logs as a CSV

### Questions
*Where Do You Think You Are Now?*
At the very first step, of only having version control (GitHub)

*What Is Your Objective?*
To build a dashboard in an iterative way and experience what having a pipeline from the start for a UI could solve with being able to pivot quickly.

*What Is Your Next Step?*
My plan is to do each step after following the course. But I think my first step will be to create placeholders in my pipeline for each of the steps.

*How Will You Know If You Have Succeeded?*
For this current step: when the pipeline runs all of the steps and outputs logs.
