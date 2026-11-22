# Production Readiness

## Current Status

`v1.0.0` is the production release candidate. It passed owner acceptance
testing and a verified Nautobot 3.2.3 deployment on August 29, 2026. Final
release publication follows the protected pull-request and tag workflow.

## Production Evidence

| Gate | Status |
| --- | --- |
| Package | Wheel and source distribution build successfully. |
| Nautobot | System check and post-upgrade complete without pending migrations. |
| Tests | 61 combined app tests pass from the exact production wheels. |
| UI and API | Dashboard, model lists, Installed App details, Device extensions, and APIs pass authenticated smoke checks. |
| Jobs and metrics | Reconciliation Job and six combined app metrics are registered and operational. |
| Operations | Web, worker, scheduler, PostgreSQL, Redis, Nginx, TLS, rollback, and backup checks pass. |
| Recovery | Failed preflight releases restored the prior packages successfully before final promotion. |

The repository owner approved preparation of Production v1.0.0 on August 29,
2026. The dependency lock was refreshed to fixed releases, including Nautobot
3.2.3, Django 5.2.17, sqlparse 0.6.0, cryptography 50.0.1, GitPython 3.1.61,
Pillow 12.3.0, and PyJWT 2.13.0. Expanded performance targets, vendor collector
selection, and migration scope must be reviewed during v2 planning on October
1, 2026.
