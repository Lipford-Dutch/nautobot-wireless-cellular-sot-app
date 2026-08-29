# Production v1.0 Release Notes

## [v1.0.0] - 2026-08-29

Production v1.0.0 promotes the Cellular source of truth to stable operation on
Nautobot 3.

### Added

- Added complete UI coverage for operational snapshots and global search for
  all four Cellular models.
- Added database-backed runtime configuration, snapshot hash validation,
  Cellular home-page content, contextual banners, reusable Jinja filters, and
  bounded-cardinality Prometheus app metrics.
- Added a registered reconciliation Job and core Device filter and table
  extensions.
- Added release checksums, wheel import validation, and GitHub artifact
  provenance attestations.

### Changed

- Renamed the primary navigation from **Wireless Infrastructure** to
  **Cellular**.
- Updated GraphQL types and Nautobot integration paths for Nautobot 3.2.
- Promoted the package version and documentation from `v0.1.0` to stable
  `v1.0.0`.

### Validation

- Passed 61 combined application tests from the exact production wheels.
- Passed Nautobot system, migration, dependency, service, HTTPS, UI, API,
  Celery, rollback, and backup checks on the production Hostinger deployment.
