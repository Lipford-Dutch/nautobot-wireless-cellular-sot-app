# External Interactions

Vendor collectors normalize Cisco, Cradlepoint, Sierra, carrier portal, or custom API payloads before reconciliation.

Sensitive ICCID, IMSI, and MSISDN values must not be emitted as Prometheus labels or unmasked general-purpose logs.

The base reconciliation Job remains dry-run-first until a vendor-specific collector is explicitly configured.
