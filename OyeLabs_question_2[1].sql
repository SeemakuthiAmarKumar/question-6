SELECT
  *
FROM
  customers
  JOIN studentsubjectmapping ON customers.customerId = studentsubjectmapping.customerId
WHERE
  customers.customerId = 1;