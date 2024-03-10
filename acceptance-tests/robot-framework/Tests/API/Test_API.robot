*** Settings ***
Library         REST

*** Test Cases ***
GET orders and validate schema
    GET         http://localhost:5000/orders
    Array    response body
    String    $[*].abbreviated_name
    String    $[*].food_ordered
    String    $[*].processing_status
    String    $[*].started_status
    String    $[*].trace_id

GET orders and validate values of first object
    GET         http://localhost:5000/orders
    String    $[0].abbreviated_name    SherlockHolmes
    String    $[0].food_ordered    Pie
    String    $[0].processing_status    True
    String    $[0].started_status    True
    String    $[0].trace_id    23404

GET orders and validate values of second object
    GET         http://localhost:5000/orders
    String    $[1].abbreviated_name    JohnWatson
    String    $[1].food_ordered    Pizza
    String  $[1].processing_status    ""
    String    $[1].started_status    False
    String    $[1].trace_id    53192