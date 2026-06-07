# Extending the App

Open an issue before adding vendor collectors, new model fields, or write-capable synchronization behavior.

## Adding a Collector

1. Normalize vendor payloads into `NormalizedCellularRouter`.
2. Reject duplicate serial numbers and IMEIs before DiffSync.
3. Keep raw vendor payloads out of Nautobot unless explicitly required.
4. Treat conflicting SIM assignments as manual-review events.

## Adding Observability

Keep Prometheus labels low-cardinality. Do not expose ICCID, IMSI, MSISDN, or raw APNs as labels.
